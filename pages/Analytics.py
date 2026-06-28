import streamlit as st
import pandas as pd
import plotly.express as px

from database.database_manager import DatabaseManager
from components.footer import show_footer

st.set_page_config(
    page_title="Analytics Lab",
    page_icon="📈",
    layout="wide"
)

st.title("📈 ORACLE Analytics Lab")
st.caption("Explore historical drawing data")

df = DatabaseManager.query("SELECT * FROM drawings")

if df.empty:
    st.warning("No data available.")
    show_footer()
    st.stop()

game = st.selectbox(
    "Choose Game",
    sorted(df["game"].unique())
)

filtered = df[df["game"] == game]

numbers = pd.concat([
    filtered["n1"],
    filtered["n2"],
    filtered["n3"],
    filtered["n4"],
    filtered["n5"]
])

frequency = (
    numbers.value_counts()
    .sort_index()
    .reset_index()
)

frequency.columns = ["Number", "Times Drawn"]

fig = px.bar(
    frequency,
    x="Number",
    y="Times Drawn",
    title=f"{game} Number Frequency"
)

st.plotly_chart(fig, use_container_width=True)

show_footer()