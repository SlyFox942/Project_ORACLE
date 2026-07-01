import streamlit as st

from config import APP_NAME, VERSION, AUTHOR
from components.header import show_header
from components.sidebar import show_sidebar
from components.footer import show_footer

st.set_page_config(
    page_title="About Project ORACLE",
    page_icon="🔮",
    layout="wide"
)

show_sidebar()
show_header()

st.header("📖 About Project ORACLE")

st.write("""
Project ORACLE is an analytics and cybersecurity platform
built entirely in Python.

It demonstrates modern software engineering practices,
interactive analytics, cybersecurity tools, and modular
application design.

The platform combines data visualization, log analysis,
file hashing, threat intelligence, and statistical
analysis into one application.
""")

st.subheader("🛠 Technologies")

st.markdown("""
- 🐍 Python
- 🎈 Streamlit
- 🗄 SQLite
- 🐼 Pandas
- 📈 Plotly
- 🔄 Git
- ☁ GitHub
- ⚙ GitHub Actions
- 🧪 PyTest
- 🏗 Modular Architecture
""")

st.subheader("👩‍💻 Author")

st.write(f"**{AUTHOR}**")

st.subheader("🚀 Current Version")

st.success(f"{APP_NAME} Version {VERSION}")

show_footer()