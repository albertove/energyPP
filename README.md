# Energy Consumption Dashboard

A comprehensive Streamlit-based web application for visualizing and analyzing energy consumption data across multiple years. This dashboard provides interactive visualizations, data management capabilities, and detailed insights into energy usage patterns.

## 🚀 Features

### 🔐 Authentication
- Secure login system with session management
- User-friendly login interface
- Session persistence across page refreshes

### 📊 Interactive Visualizations
- **Monthly Trends**: Multi-year comparison of monthly consumption patterns
- **Yearly Analysis**: Detailed time series visualization for selected years
- **Weekly Analysis**: Minimum and maximum consumption analysis with day-of-week indicators
- **Real-time Updates**: Dynamic charts that update with new data

### 📈 Advanced Analytics
- **Multi-Year Weekly Statistics**: Comprehensive min/max consumption analysis with averages
- **Statistical Measures**: Average min/max consumption, overall extremes
- **Monthly Aggregation**: Monthly trend analysis and comparisons
- **Year-over-Year Comparisons**: Multi-year weekly statistics comparison
- **Interactive Data Points**: Hover information and detailed breakdowns

### 📤 Data Management
- **File Upload**: Easy upload of new Excel data files
- **Automatic Processing**: Real-time data processing and analysis
- **File Management**: View, delete, and manage data files
- **Download Functionality**: Export processed data and summaries
- **Data Validation**: Comprehensive error handling and validation

### 🔄 Real-time Features
- **Refresh Dashboard**: Update visualizations with new data
- **Dynamic Year Support**: Automatic detection of current year and available data files
- **File Status Indicators**: Visual feedback for upload operations
- **Error Handling**: Robust error management and user feedback
- **Year Transition Management**: Automatic handling of year transitions (e.g., 2025 → 2026)

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Windows/Linux/macOS compatible

## 📦 Installation

1. **Clone the repository**:
```bash
git clone <repository-url>
cd energyPP
```

2. **Install required dependencies**:
```bash
pip install -r requirements.txt
```

3. **Create data directory** (if not exists):
```bash
mkdir data
```

## 🗂️ Data Format Requirements

### File Naming Convention
Excel files must follow this naming pattern:
```
El-YYYY-01-01-YYYY-12-31.xlsx
```
Example: `El-2024-01-01-2024-12-31.xlsx`

### Excel File Structure
Each Excel file must contain:
- **Sheet Name**: "Timvärden" (Swedish for "Time Values")
- **Header Row**: Data starts from row 17 (header=16 in pandas)
- **Required Columns**:
  - `Datum och tid` (Date and time) - DateTime format
  - `Förbrukning` (Consumption) - Numeric values in kWh

### Sample Data Structure
```
| Datum och tid          | Förbrukning |
|------------------------|-------------|
| 2024-01-01 00:00:00    | 125.5       |
| 2024-01-01 01:00:00    | 118.2       |
| ...                    | ...         |
```

## 🚀 Usage

### Starting the Application
```bash
streamlit run app.py
```

### Accessing the Dashboard
1. Open your web browser
2. Navigate to `http://localhost:8501`
3. Login with credentials:
   - **Username**: `admin`
   - **Password**: `admin123`

### Using the Dashboard

#### 📊 Main Dashboard Features
- **Monthly Trends Chart**: View consumption patterns across multiple years
- **Year Selection**: Choose specific year for detailed analysis
- **Yearly Consumption Chart**: Interactive time series for selected year
- **Weekly Analysis Chart**: Min/max consumption per week with day indicators
- **Multi-Year Comparison Table**: Compare weekly statistics across different years

#### 🔧 Sidebar Functions
- **File Upload/Update**: Upload Excel files for any year (current or historical)
- **Year Selection**: Choose which year to upload or update data for (2020 to current year)
- **Data Replacement**: Replace existing year data with new files
- **Replacement Confirmation**: Safety checkbox to confirm data replacement
- **Refresh Data**: Update dashboard with latest data
- **File Management**: View and delete existing data files
- **Download**: Export updated data files
- **Year Validation**: Automatic checking for missing previous year data
- **Logout**: Secure session termination

#### 📁 File Management
- **Upload Status**: Visual indicators for successful uploads
- **File List**: View all available data files by year
- **Delete Files**: Remove unwanted data files
- **Download Updated Files**: Export processed data

#### 📊 Data Tables & Statistics
- **Multi-Year Comparison Table**: Compare weekly statistics across all available years
- **Statistical Measures**: Average min/max consumption, overall extremes

## 🔧 Technical Details

### Dependencies
- **pandas** (≥1.5.0): Data manipulation and analysis
- **streamlit** (≥1.22.0): Web application framework
- **plotly** (≥5.13.0): Interactive visualizations
- **openpyxl** (≥3.1.0): Excel file handling

### Data Processing Pipeline
1. **Dynamic File Discovery**: Automatically scans `data/` directory for available years
2. **File Loading**: Reads Excel files from `data/` directory based on discovered files
3. **Data Validation**: Checks file format and data integrity
4. **Data Transformation**: Converts timestamps and calculates derived fields
5. **Statistical Analysis**: Computes weekly min/max/average consumption
6. **Visualization**: Generates interactive charts with Plotly
7. **Summary Generation**: Creates "Sammanfatning" sheet with processed data
8. **Year Transition Handling**: Automatically manages year transitions and missing data

### File Structure
```
energyPP/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── README.md             # This documentation
├── LICENSE               # MIT License
└── data/                 # Data directory
    ├── El-2020-01-01-2020-12-31.xlsx
    ├── El-2021-01-01-2021-12-31.xlsx
    ├── El-2022-01-01-2022-12-31.xlsx
    ├── El-2023-01-01-2023-12-31.xlsx
    ├── El-2024-01-01-2024-12-31.xlsx
    └── El-2025-01-01-2025-12-31.xlsx
```

## 🛡️ Security Considerations

⚠️ **Important Security Note**: The current login system uses hardcoded credentials for demonstration purposes only. For production deployment, implement:
- Secure authentication (OAuth, JWT tokens)
- Password hashing and encryption
- Session management with proper security headers
- HTTPS encryption
- Input validation and sanitization

## 🔄 Year Transition Management

### Automatic Year Handling
The application automatically handles year transitions and manages data files dynamically:

#### **For 2026 Usage (Example)**
When the application runs in 2026:
1. **Current Year Detection**: Automatically detects 2026 as the current year
2. **Available Years Scan**: Scans the `data/` folder for all available year files
3. **Missing Year Detection**: Shows warning if 2025 data is missing
4. **Flexible Upload**: Allows uploading data for any year (2025, 2026, or historical years)
5. **Dynamic Loading**: Loads all available years automatically without hardcoded paths

#### **Year Transition Workflow**
```
2025 → 2026 Transition:
├── ✅ 2025 data exists → Shows success message
├── ⚠️ 2025 data missing → Shows warning to upload first
├── 📤 Upload 2025 data → Select year 2025 in dropdown
├── 📤 Upload 2026 data → Select year 2026 in dropdown
└── 🔄 Refresh → Updates dashboard with all available years
```

#### **Dynamic File Management**
- **No Hardcoded Years**: Application discovers years automatically
- **Flexible Upload/Update**: Upload or replace data for any year from 2020 to current year
- **Data Replacement Safety**: Confirmation checkbox when replacing existing data
- **Missing Data Alerts**: Warns when previous year data is missing
- **Automatic Integration**: New years are automatically included in visualizations
- **Clear Status Indicators**: Shows whether you're adding new data or replacing existing data

## 🐛 Troubleshooting

### Common Issues

**File Upload Errors**:
- Ensure Excel file follows naming convention
- Check that "Timvärden" sheet exists
- Verify data starts from row 17
- Confirm required columns are present

**Year Transition Issues**:
- If previous year data is missing, upload it first
- Use the year selector in the sidebar to choose the correct year
- Check that file naming follows the exact pattern: `El-YYYY-01-01-YYYY-12-31.xlsx`

**Data Replacement Issues**:
- When replacing existing data, make sure to check the confirmation checkbox
- The system will warn you before replacing existing year data
- Always verify the year selection before uploading

**Data Display Issues**:
- Click "Refresh Dashboard Data" after uploading
- Check file format and data integrity
- Ensure no empty cells in consumption column

**Performance Issues**:
- Large datasets may take time to process
- Consider data sampling for very large files
- Monitor memory usage with extensive datasets

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/AmazingFeature`
3. **Commit your changes**: `git commit -m 'Add some AmazingFeature'`
4. **Push to the branch**: `git push origin feature/AmazingFeature`
5. **Open a Pull Request**

### Development Guidelines
- Follow PEP 8 Python style guidelines
- Add comprehensive error handling
- Include docstrings for new functions
- Test with various data formats
- Update documentation as needed

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Streamlit**: For the powerful web application framework
- **Plotly**: For interactive data visualizations
- **Pandas**: For robust data processing capabilities
- **OpenPyXL**: For Excel file handling

## 📞 Support

For questions, issues, or feature requests, please:
- Open an issue on GitHub
- Check the troubleshooting section
- Review the documentation thoroughly

---

**Version**: 1.0.0  
**Last Updated**: 2024  
**Compatibility**: Python 3.7+, Streamlit 1.22+ 
