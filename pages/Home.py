import streamlit as st
from config import APP_NAME, VERSION
from components.footer import show_footer

st.set_page_config(
    page_title=APP_NAME,
    page_icon="🔮",
    layout="wide"
)

st.title("🔮 Project ORACLE")
st.subheader("Lottery Analytics & Research Platform")

st.markdown(
    """
Welcome to **Project ORACLE**.

This application explores historical lottery drawing data using Python,
SQLite, Pandas, and Plotly.

### Quick Links

- 📊 Executive Dashboard
- 📥 Import Data
- 🗄 Database Explorer
- 🩺 Database Health
- 🤖 ORACLE Insights
- 🎲 Predictions
"""
)

st.info(
    "This project is for statistical analysis and educational purposes only."
)

show_footer()