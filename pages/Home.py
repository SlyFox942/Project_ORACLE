import streamlit as st
from pathlib import Path

from config import APP_NAME, VERSION
from components.footer import show_footer

st.set_page_config(
    page_title=APP_NAME,
    page_icon="assets/oracle_icon.png",
    layout="wide"
)

banner = Path("assets/oracle_banner.png")
logo = Path("assets/oracle_full_logo.png")

if banner.exists():
    st.image(str(banner), use_container_width=True)

left, right = st.columns([1,2])

with left:

    if logo.exists():
        st.image(str(logo), width=260)

with right:

    st.title("🔮 Project ORACLE")

    st.markdown("## Data Analytics • Software Engineering • Cybersecurity")

    st.success("### Turning Data Into Insight")

    st.write(
        """
Project ORACLE is a modern analytics platform built with Python,
Streamlit, SQLite, Plotly and Pandas.

Originally created as a lottery analytics platform,
ORACLE has evolved into a showcase of software engineering,
interactive dashboards, statistical analysis, and future
cybersecurity tooling.
"""
    )

st.divider()

st.subheader("🚀 Explore ORACLE")

c1, c2, c3 = st.columns(3)

with c1:

    st.page_link("pages/Executive_Dashboard.py",
                 label="📊 Executive Dashboard")

    st.page_link("pages/Statistics.py",
                 label="📈 Statistics")

    st.page_link("pages/Heat_Map.py",
                 label="🔥 Heat Map")

with c2:

    st.page_link("pages/Database_Explorer.py",
                 label="🗄 Database Explorer")

    st.page_link("pages/Database_Health.py",
                 label="🩺 Database Health")

    st.page_link("pages/Data_Import.py",
                 label="📥 Import Data")

with c3:

    st.page_link("pages/Oracle_AI.py",
                 label="🤖 ORACLE AI")

    st.page_link("pages/Predictions.py",
                 label="🎲 Predictions")

show_footer()