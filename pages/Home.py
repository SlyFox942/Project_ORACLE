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

col1, col2 = st.columns([1, 2])

with col1:
    if logo.exists():
        st.image(str(logo), width=260)

with col2:
    st.title("🔮 Project ORACLE")
    st.markdown("### Analytics • Cybersecurity • Intelligence")
    st.success("Turning Data Into Insight")
    st.write(
        """
        Project ORACLE is a Python analytics and cybersecurity platform
        built with Streamlit, SQLite, Pandas, Plotly, GitHub Actions,
        and modular software architecture.
        """
    )
    st.caption(f"Version {VERSION}")

st.divider()

st.subheader("🚀 Choose Your Lab")

a1, a2 = st.columns(2)

with a1:
    st.markdown("## 📊 Analytics Lab")
    st.write("Explore historical data, dashboards, predictions, trends, and visual insights.")
    st.page_link("pages/Executive_Dashboard.py", label="📊 Executive Dashboard")
    st.page_link("pages/Analytics_Lab.py", label="📈 Analytics Lab")
    st.page_link("pages/Predictions.py", label="🎲 Predictions")
    st.page_link("pages/Oracle_Score.py", label="🔮 ORACLE Score")

with a2:
    st.markdown("## 🛡 Cyber Lab")
    st.write("Analyze logs, hashes, indicators, MITRE mappings, and threat signals.")
    st.page_link("pages/Log_Analyzer.py", label="📄 SOC Log Analyzer")
    st.page_link("pages/File_Hash_Generator.py", label="🔐 File Hash Generator")
    st.page_link("pages/Hash_History.py", label="📝 Hash History")
    st.page_link("pages/Threat_Dashboard.py", label="🛡 Threat Dashboard")

st.divider()

st.subheader("🗄 Data & System")

d1, d2, d3 = st.columns(3)

with d1:
    st.page_link("pages/Data_Import.py", label="📥 Data Import")

with d2:
    st.page_link("pages/Database_Explorer.py", label="🗄 Database Explorer")

with d3:
    st.page_link("pages/Database_Health.py", label="🩺 Database Health")

show_footer()