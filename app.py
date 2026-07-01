import streamlit as st
from utils.theme import load_css
from pathlib import Path
import streamlit as st
from components.sidebar import show_sidebar

st.set_page_config(
    page_title="Project ORACLE",
    page_icon="assets/oracle_icon.png",
    layout="wide"
)

logo = Path("assets/oracle_icon.png")

if logo.exists():
    st.logo(str(logo))
    
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
from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="Project ORACLE",
    page_icon="assets/oracle_icon.png",
    layout="wide"
)

logo = Path("assets/oracle_icon.png")

if logo.exists():
    st.logo(str(logo))