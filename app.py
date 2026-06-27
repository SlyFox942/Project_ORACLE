import streamlit as st
from utils.theme import load_css

st.set_page_config(
    page_title="Project ORACLE",
    page_icon="🔮",
    layout="wide"
)

load_css()

st.title("🔮 Project ORACLE")

st.subheader("Lottery Analytics & AI Research Lab")

st.success("Welcome to ORACLE!")

st.markdown("""
## Welcome

Project ORACLE is a research platform for:

- 🎱 Mega Millions
- 🔴 Powerball
- 📊 Statistical Analysis
- 🤖 AI Experiments
- 🎲 Monte Carlo Simulations
- 🧪 Strategy Testing

Choose a page from the sidebar to begin.
""")