# Energy Consumption Dashboard

A Streamlit-based web application for visualizing and analyzing energy consumption data across multiple years. This dashboard provides interactive visualizations and insights into energy usage patterns.

## Features

- 🔐 Secure login system
- 📊 Interactive visualizations:
  - Monthly consumption trends across multiple years
  - Yearly consumption patterns
  - Weekly minimum and maximum consumption analysis
- 📈 Data analysis capabilities:
  - Weekly consumption statistics
  - Monthly aggregation
  - Year-over-year comparisons
- 📤 Data management:
  - Easy upload of new data files
  - Automatic data processing and analysis
  - Download functionality for processed data

## Prerequisites

- Python 3.7+
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/energy-consumption-dashboard.git
cd energy-consumption-dashboard
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Required Dependencies

- pandas
- streamlit
- plotly
- openpyxl

## Data Format

The application expects Excel files with the following naming convention:
- `El-YYYY-01-01-YYYY-12-31.xlsx`

Each Excel file should contain:
- A sheet named "Timvärden" with energy consumption data
- Data should start from row 17 (header row)
- Required columns:
  - "Datum och tid" (Date and time)
  - "Förbrukning" (Consumption)

## Usage

1. Start the application:
```bash
streamlit run app.py
```

2. Access the dashboard through your web browser (typically at http://localhost:8501)

3. Login credentials:
   - Username: admin
   - Password: admin123

4. Use the sidebar to:
   - Upload new data files
   - Download processed data
   - Logout from the application

## Features in Detail

### Monthly Trends
- Visualizes consumption patterns across different months
- Compares data across multiple years
- Interactive hover information

### Yearly Analysis
- Detailed view of consumption for selected year
- Interactive time series visualization
- Easy year selection

### Weekly Analysis
- Shows minimum and maximum consumption per week
- Displays day of occurrence for peak values
- Bar chart visualization for easy comparison

## Security Note

The current login system is for demonstration purposes only. In a production environment, implement proper authentication and security measures.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with Streamlit
- Data visualization powered by Plotly
- Data processing with Pandas 
