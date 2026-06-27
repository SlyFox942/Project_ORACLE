import streamlit as st
import pandas as pd
import plotly.express as px

from database.database_manager import DatabaseManager
from components.footer import show_footer

st.title("🔮 Project ORACLE")
st.caption("Lottery Analytics & Research Platform")

df = DatabaseManager.query("SELECT * FROM drawings")

total = len(df)
mega = len(df[df["game"] == "Mega Millions"])
power = len(df[df["game"] == "Powerball"])

col1, col2, col3, col4 = st.columns(4)

col1.metric("📊 Total Drawings", total)
col2.metric("🎱 Mega Millions", mega)
col3.metric("🔴 Powerball", power)
col4.metric("🟢 Database", "Connected")

st.divider()

if not df.empty:
    numbers = pd.concat([df["n1"], df["n2"], df["n3"], df["n4"], df["n5"]])

    frequency = numbers.value_counts().sort_index().reset_index()
    frequency.columns = ["Number", "Times Drawn"]

    fig = px.bar(
        frequency,
        x="Number",
        y="Times Drawn",
        title="📈 Number Frequency"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("🔥 Top 10 Hot Numbers")
    st.dataframe(
        frequency.sort_values("Times Drawn", ascending=False).head(10),
        width="stretch"
    )

    st.subheader("📅 Latest Drawings")
    st.dataframe(
        df.sort_values("draw_date", ascending=False),
        width="stretch"
    )
else:
    st.warning("Database is empty.")

show_footer()