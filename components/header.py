import streamlit as st
from pathlib import Path

from config import APP_NAME, VERSION, APP_DESCRIPTION


def show_header():

    banner = Path("assets/oracle_banner.png")
    logo = Path("assets/oracle_full_logo.png")

    if banner.exists():
        st.image(str(banner), use_container_width=True)

    left, right = st.columns([1, 3])

    with left:
        if logo.exists():
            st.image(str(logo), width=180)

    with right:
        st.title(APP_NAME)
        st.markdown(f"### {APP_DESCRIPTION}")
        st.caption(f"Version {VERSION}")

    st.divider()