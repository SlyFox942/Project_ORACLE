import streamlit as st


def status_card(title, status, color="green"):
    if color == "green":
        icon = "🟢"
    elif color == "yellow":
        icon = "🟡"
    elif color == "red":
        icon = "🔴"
    else:
        icon = "⚪"

    st.markdown(
        f"""
### {icon} {title}

**Status:** {status}
"""
    )