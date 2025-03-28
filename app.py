import pandas as pd
import streamlit as st
import plotly.express as px
from datetime import datetime
import os
import io

# Set page config
st.set_page_config(page_title="Energy Consumption Dashboard", layout="wide")

# Initialize session state for login
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Login function
def login(username, password):
    # This is a simple example. In a real application, you should use secure authentication
    if username == "admin" and password == "admin123":
        st.session_state.logged_in = True
        return True
    return False

# Login page
if not st.session_state.logged_in:
    st.title("Login")
    
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit_button = st.form_submit_button("Login")
        
        if submit_button:
            if login(username, password):
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Invalid username or password")
    
    st.stop()

# Get current year
current_year = datetime.now().year

# Load the Excel files
file_2020 = "El-2020-01-01-2020-12-31.xlsx"
file_2021 = "El-2021-01-01-2021-12-31.xlsx"
file_2022 = "El-2022-01-01-2022-12-31.xlsx"
file_2023 = "El-2023-01-01-2023-12-31.xlsx"
file_2024 = 'El-2024-01-01-2024-12-31.xlsx'
file_current = f'El-{current_year}-01-01-{current_year}-12-31.xlsx'

# Add logout button in sidebar
with st.sidebar:
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()
    
    st.header("Update Current Year Data")
    st.write(f"Current year: {current_year}")
    
    uploaded_file = st.file_uploader(
        f"Upload new data for {current_year}",
        type=['xlsx'],
        help=f"Upload the Excel file named 'El-{current_year}-01-01-{current_year}-12-31.xlsx'"
    )
    
    if uploaded_file is not None:
        try:
            # Read the uploaded file
            new_data = pd.read_excel(uploaded_file, sheet_name="Timvärden", header=16)
            
            # Save the file
            with open(file_current, 'wb') as f:
                f.write(uploaded_file.getvalue())
            
            # Process the new data for Sammanfatning sheet
            new_data['Datum och tid'] = pd.to_datetime(new_data['Datum och tid'], errors='coerce')
            new_data['Year'] = new_data['Datum och tid'].dt.year
            new_data['Week'] = new_data['Datum och tid'].dt.isocalendar().week
            new_data = new_data.rename(columns={'Förbrukning': 'Consumption'})
            new_data = new_data.dropna(subset=['Consumption'])
            
            # Calculate statistics for the new data
            min_consumption = new_data.loc[new_data.groupby('Week')['Consumption'].idxmin()]
            max_consumption = new_data.loc[new_data.groupby('Week')['Consumption'].idxmax()]
            avg_consumption = new_data.groupby('Week')['Consumption'].mean().reset_index()
            avg_consumption.rename(columns={'Consumption': 'Average Consumption'}, inplace=True)
            
            # Create result DataFrame for Sammanfatning sheet
            result = min_consumption[['Week', 'Datum och tid', 'Consumption']].reset_index(drop=True)
            result.rename(columns={'Week': 'Week Number', 'Consumption': 'Minimum Consumption', 
                                 'Datum och tid': 'Min Date and Time'}, inplace=True)
            
            # Add maximum consumption data
            max_consumption = max_consumption[['Week', 'Consumption', 'Datum och tid']].reset_index(drop=True)
            max_consumption.rename(columns={'Consumption': 'Maximum Consumption', 
                                         'Datum och tid': 'Max Date and Time',
                                         'Week': 'Week Number'}, inplace=True)
            result = result.merge(max_consumption, on='Week Number')
            
            # Add average consumption data
            result = result.merge(avg_consumption, left_on='Week Number', right_on='Week')
            
            # Add Year column
            result['Year'] = current_year
            
            # Save to Sammanfatning sheet
            with pd.ExcelWriter(file_current, mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                result.to_excel(writer, sheet_name='Sammanfatning', index=False)
            
            st.success(f"Successfully updated data and Sammanfatning sheet for {current_year}!")
            
            # Add download button after successful update
            with open(file_current, 'rb') as f:
                st.download_button(
                    label=f"Download Updated {current_year} Data",
                    data=f,
                    file_name=file_current,
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
            
            st.rerun()  # Rerun to refresh the data
        except Exception as e:
            st.error(f"Error updating file: {str(e)}")

# Define file paths (excluding current year file if it doesn't exist)
file_paths = [file_2020, file_2021, file_2022, file_2023, file_2024]

# Load the specific sheet "Timvärden" from all files
data_frames = []
for file_path in file_paths:
    try:
        df = pd.read_excel(file_path, sheet_name="Timvärden", header=16)
        data_frames.append(df)
    except FileNotFoundError:
        st.warning(f"File not found: {file_path}")

# Try to load current year file if it exists
try:
    current_year_df = pd.read_excel(file_current, sheet_name="Timvärden", header=16)
    data_frames.append(current_year_df)
except FileNotFoundError:
    st.info(f"Current year file ({file_current}) not found. You can upload it using the sidebar.")

# Combine all dataframes
combined_data = pd.concat(data_frames, ignore_index=True)

# Convert the "Datum och tid" column to datetime format
combined_data['Datum och tid'] = pd.to_datetime(combined_data['Datum och tid'], errors='coerce')

# Extract the year, month, and week number from the "Datum och tid" column
combined_data['Year'] = combined_data['Datum och tid'].dt.year
combined_data['Year'] = combined_data['Year'].fillna(0).astype(int)
combined_data['Month'] = combined_data['Datum och tid'].dt.month
combined_data['Week'] = combined_data['Datum och tid'].dt.isocalendar().week
combined_data['Week'] = combined_data['Week'].fillna(0).astype(int)
combined_data['Month_Name'] = combined_data['Datum och tid'].dt.strftime('%B')

# Rename Förbrukning to Consumption
combined_data = combined_data.rename(columns={'Förbrukning': 'Consumption'})

# Drop any rows with NaN values in the 'Consumption' column
filtered_data = combined_data.dropna(subset=['Consumption'])

# Find the minimum and maximum consumption for each week
min_consumption_per_week = filtered_data.loc[filtered_data.groupby(['Year', 'Week'])['Consumption'].idxmin()]
min_consumption_per_week['Day'] = min_consumption_per_week['Datum och tid'].dt.strftime('%a')
max_consumption_per_week = filtered_data.loc[filtered_data.groupby(['Year', 'Week'])['Consumption'].idxmax()]
max_consumption_per_week['Day'] = max_consumption_per_week['Datum och tid'].dt.strftime('%a')

# Calculate average consumption for each week
average_consumption_per_week = filtered_data.groupby(['Year', 'Week'])['Consumption'].mean().reset_index()
average_consumption_per_week.rename(columns={'Consumption': 'Average Consumption'}, inplace=True)

# Create weekly_consumption DataFrame for the weekly chart
weekly_consumption = pd.merge(min_consumption_per_week, max_consumption_per_week, on=['Year', 'Week'], suffixes=('_Min', '_Max'))
weekly_consumption = weekly_consumption[['Year', 'Week', 'Consumption_Min', 'Consumption_Max', 'Day_Min', 'Day_Max']]
weekly_consumption.rename(columns={'Day_Min': 'Min Day', 'Day_Max': 'Max Day'}, inplace=True)

# Streamlit UI
st.title("Energy Consumption Dashboard")

# Create and display monthly consumption trends across multiple years
monthly_trends = filtered_data.groupby(['Year', 'Month_Name'])['Consumption'].sum().reset_index()
monthly_trends['Year'] = monthly_trends['Year'].astype(int)
monthly_trends['Month'] = pd.Categorical(monthly_trends['Month_Name'], categories=[
    'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'
], ordered=True)
monthly_trends = monthly_trends.sort_values(['Year', 'Month'])  # Sort by both Year and Month

monthly_fig = px.line(monthly_trends, x='Month', y='Consumption', color='Year',
                      title='Comparison Of Monthly Energy Consumption Trends Across Multiple Years',
                      labels={'Month': 'Month', 'Consumption': 'Consumption (kWh)', 'Year': 'Year'},
                      template='simple_white')
monthly_fig.update_layout(title_x=0.5, font=dict(family="Arial", size=14),
                         xaxis_title='Month', yaxis_title='Consumption (kWh)')
# Update the legend to show years in chronological order
monthly_fig.update_layout(legend_traceorder="normal")
st.plotly_chart(monthly_fig, use_container_width=True)

# Year selector with valid years only
valid_years = sorted(filtered_data['Year'].unique())
selected_year = st.selectbox(
    "Select Year:",
    options=valid_years,
    index=len(valid_years)-1  # Default to the most recent year
)

# Filter data for the selected year
yearly_data = filtered_data[filtered_data['Year'] == selected_year]
weekly_data = weekly_consumption[weekly_consumption['Year'] == selected_year]

# Create and display yearly consumption line chart
yearly_fig = px.line(yearly_data, x='Datum och tid', y='Consumption', 
                     title=f'Yearly Energy Consumption for {selected_year}',
                     template='simple_white')
yearly_fig.update_layout(title_x=0.5, font=dict(family="Arial", size=14), 
                        xaxis_title='Time', yaxis_title='Consumption (kWh)')
st.plotly_chart(yearly_fig, use_container_width=True)

# Create and display weekly min and max consumption chart
weekly_fig = px.bar(weekly_data, x='Week', y=['Consumption_Min', 'Consumption_Max'],
                    labels={'Week': 'Week Number', 'value': 'Consumption (kWh)', 'variable': 'Consumption Type'},
                    title=f'Weekly Minimum and Maximum Consumption for {selected_year}',
                    barmode='group', template='simple_white')
weekly_fig.update_layout(title_x=0.5, font=dict(family="Arial", size=14),
                        xaxis_title='Week Number', yaxis_title='Consumption (kWh)',
                        xaxis=dict(tickmode='linear', dtick=1))
weekly_fig.update_traces(textposition='outside')
weekly_fig.update_traces(selector=dict(name='Consumption_Min'), text=weekly_data['Min Day'],
                        textposition='inside', textangle=-90)
weekly_fig.update_traces(selector=dict(name='Consumption_Max'), text=weekly_data['Max Day'],
                        textposition='inside', textangle=-90)
st.plotly_chart(weekly_fig, use_container_width=True)

