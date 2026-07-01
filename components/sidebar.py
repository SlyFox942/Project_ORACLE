import streamlit as st
from config import APP_NAME, VERSION


def show_sidebar():
    with st.sidebar:
        st.image("assets/oracle_icon.png", width=90)

        st.title(APP_NAME)
        st.caption(f"Version {VERSION}")

        st.divider()

        st.markdown("### 📊 Analytics")
        st.page_link("pages/Executive_Dashboard.py", label="Executive Dashboard")
        st.page_link("pages/Analytics_Lab.py", label="Analytics Lab")
        st.page_link("pages/Oracle_Score.py", label="ORACLE Score")
        st.page_link("pages/Predictions.py", label="Predictions")

        st.divider()

        st.markdown("### 🛡 Cyber Lab")
        st.page_link("pages/Log_Analyzer.py", label="SOC Log Analyzer")
        st.page_link("pages/File_Hash_Generator.py", label="File Hash Generator")
        st.page_link("pages/Hash_History.py", label="Hash History")
        st.page_link("pages/MITRE_Explorer.py", label="MITRE Explorer")
        st.page_link("pages/Threat_Dashboard.py", label="Threat Dashboard")
        st.page_link("pages/ORACLE_Assistant.py", label="ORACLE Assistant")

        st.divider()

        st.markdown("### 🗄 Database")
        st.page_link("pages/Data_Import.py", label="Data Import")
        st.page_link("pages/Database_Explorer.py", label="Database Explorer")
        st.page_link("pages/Database_Health.py", label="Database Health")