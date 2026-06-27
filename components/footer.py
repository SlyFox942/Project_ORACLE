import streamlit as st

from config import VERSION, AUTHOR


def show_footer():

    st.divider()

    st.caption(
        f"🔮 Project ORACLE {VERSION} | "
        f"Built by {AUTHOR} | "
        "Educational analytics project."
    )