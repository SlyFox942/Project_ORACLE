import streamlit as st
from config import VERSION
from components.footer import show_footer

st.title("ℹ️ About Project ORACLE")

st.markdown(f"""
## Version

**{VERSION}**

## Purpose

Project ORACLE demonstrates:

- Python programming
- SQLite databases
- Data visualization
- Software architecture
- Statistical analysis
- Git & GitHub workflow

This application is intended for educational and analytical purposes.
""")

show_footer()