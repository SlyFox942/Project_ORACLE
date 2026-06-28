import streamlit as st
from config import VERSION, AUTHOR

def show_footer():
    st.divider()

    st.caption(
        f"🔮 Project ORACLE v{VERSION} • Built by {AUTHOR}"
    )

    st.caption(
        "Turning Data Into Insight • Educational Analytics Platform"
    )