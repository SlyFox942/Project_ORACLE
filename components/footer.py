import streamlit as st
from config import VERSION, AUTHOR

def show_footer():

    st.divider()

    st.caption(
        f"🔮 Project ORACLE • Version {VERSION}"
    )

    st.caption(
        "Data Analytics • Software Engineering • Cybersecurity"
    )

    st.caption(
        "Turning Data Into Insight"
    )

    st.caption(
        f"Built by {AUTHOR}"
    )