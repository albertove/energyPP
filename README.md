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
- Weekly consumption statistics (min, max, average)
- Monthly aggregation and trend analysis
- Year-over-year consumption comparisons
- Interactive hover information and data points

### 📤 Data Management
- **File Upload**: Easy upload of new Excel data files
- **Automatic Processing**: Real-time data processing and analysis
- **File Management**: View, delete, and manage data files
- **Download Functionality**: Export processed data and summaries
- **Data Validation**: Comprehensive error handling and validation

### 🔄 Real-time Features
- **Refresh Dashboard**: Update visualizations with new data
- **Dynamic Year Support**: Automatic detection of current year
- **File Status Indicators**: Visual feedback for upload operations
- **Error Handling**: Robust error management and user feedback

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

#### 🔧 Sidebar Functions
- **File Upload**: Upload new Excel files for current year
- **Refresh Data**: Update dashboard with latest data
- **File Management**: View and delete existing data files
- **Download**: Export updated data files
- **Logout**: Secure session termination

#### 📁 File Management
- **Upload Status**: Visual indicators for successful uploads
- **File List**: View all available data files by year
- **Delete Files**: Remove unwanted data files
- **Download Updated Files**: Export processed data

## 🔧 Technical Details

### Dependencies
- **pandas** (≥1.5.0): Data manipulation and analysis
- **streamlit** (≥1.22.0): Web application framework
- **plotly** (≥5.13.0): Interactive visualizations
- **openpyxl** (≥3.1.0): Excel file handling

### Data Processing Pipeline
1. **File Loading**: Reads Excel files from `data/` directory
2. **Data Validation**: Checks file format and data integrity
3. **Data Transformation**: Converts timestamps and calculates derived fields
4. **Statistical Analysis**: Computes weekly min/max/average consumption
5. **Visualization**: Generates interactive charts with Plotly
6. **Summary Generation**: Creates "Sammanfatning" sheet with processed data

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

## 🐛 Troubleshooting

### Common Issues

**File Upload Errors**:
- Ensure Excel file follows naming convention
- Check that "Timvärden" sheet exists
- Verify data starts from row 17
- Confirm required columns are present

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
