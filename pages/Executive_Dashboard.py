import streamlit as st
import pandas as pd
import plotly.express as px

from database.database_manager import DatabaseManager
from components.footer import show_footer
from analysis.insights import generate_insights

st.set_page_config(
    page_title="Executive Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Executive Dashboard")
st.caption("Project ORACLE Intelligence Center")

df = DatabaseManager.query("SELECT * FROM drawings")

if df.empty:
    st.warning("Database is empty.")
    show_footer()
    st.stop()

insights = generate_insights(df)

total = len(df)
mega = len(df[df["game"] == "Mega Millions"])
power = len(df[df["game"] == "Powerball"])

numbers = pd.concat([df["n1"], df["n2"], df["n3"], df["n4"], df["n5"]])
frequency = numbers.value_counts().sort_values(ascending=False)

c1, c2, c3, c4 = st.columns(4)
c1.metric("📊 Drawings", total)
c2.metric("🎱 Mega", mega)
c3.metric("🔴 Powerball", power)
c4.metric("🔥 Hottest", insights["hottest_number"])

st.divider()

st.subheader("🔮 ORACLE Insights")

i1, i2, i3 = st.columns(3)
i1.metric("❄️ Coldest Number", insights["coldest_number"])
i2.metric("➕ Avg Draw Sum", insights["average_draw_sum"])
i3.metric("⚖️ Odd / Even", f'{insights["odd_numbers"]} / {insights["even_numbers"]}')

st.divider()

left, right = st.columns([2, 1])

chart = frequency.sort_index().reset_index()
chart.columns = ["Number", "Times Drawn"]

with left:
    fig = px.bar(
        chart,
        x="Number",
        y="Times Drawn",
        title="Number Frequency"
    )
    st.plotly_chart(fig, use_container_width=True)

with right:
    st.subheader("🔥 Top Numbers")
    st.dataframe(
        chart.sort_values("Times Drawn", ascending=False).head(10),
        use_container_width=True
    )

st.divider()

st.subheader("📅 Latest Drawings")
st.dataframe(
    df.sort_values("draw_date", ascending=False).head(20),
    use_container_width=True
)

show_footer()