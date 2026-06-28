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

if logo.exists():
    st.image(str(logo), width=260)

st.title("Project ORACLE")
st.subheader("Turning Data Into Insight")