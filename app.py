import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Fee Calculator Project Overview", layout="wide")

# Title and Subtitle
st.title("Jordan & Skala Fee Calculator Project")
st.subheader("An innovative tool for efficient fee calculations.")

# Introduction Section
st.markdown("""
## Project Description
This project automates the calculation of fees for various project types, reducing manual effort and ensuring accuracy.
The tool is designed for use by **Jordan & Skala Engineers**, leveraging a JSON-based dynamic rates system and a user-friendly interface.
""")

# Features Section
st.markdown("""
## Features
- Support for multiple project types:
  - Garden Apartments
  - High-Density Apartments
  - High-Rise Apartments
  - Retail Projects
  - Office Buildings
  - Assisted Living Facilities
- Dynamic JSON-based rate configuration.
- Detailed adders and percentage-based calculations.
- Support for PDF/Word proposal generation.
- Administrator panel for rate management.
""")

# Workflow Section
st.markdown("""
## How It Works
1. Users select the project type and enter relevant details (e.g., unit types, GSF).
2. The app calculates fees dynamically using pre-configured rates stored in a JSON file.
3. Users can add specific features or modifiers (adders).
4. A final proposal can be downloaded in PDF/Word format.
""")

# Technology Stack Section
st.markdown("""
## Technology Stack
- **Frontend**: Streamlit
- **Backend**: Python
- **Data Management**: Firebase
- **File Management**: JSON for dynamic rates configuration
""")

# Data Management Section
st.markdown("""
## Data Management
All rates and calculation logic are stored in a `rates.json` file, making the system dynamic and easy to update. The admin panel allows authorized users to update rates without modifying the codebase.
""")

# Future Enhancements Section
st.markdown("""
## Future Enhancements
- Support for additional project types.
- Enhanced reporting and analytics.
- AI-powered proposal generation using historical data.
""")

# Team Section (Optional)
st.markdown("""
## Team
- **Developer**: Dausen Mason, Tripp Davies, Adam Schick
""")
