import streamlit as st

from config import APP_NAME, VERSION, AUTHOR


def show_footer():
    st.divider()
    st.caption(
        f"🔮 {APP_NAME} • Version {VERSION} • © 2026 {AUTHOR}"
    )