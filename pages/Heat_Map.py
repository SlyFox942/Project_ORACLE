import streamlit as st
import plotly.express as px

from analysis.frequency import get_number_frequency

st.title("🔥 Number Heat Map")

game = st.selectbox(
    "Choose Game",
    ["Mega Millions", "Powerball"],
    key="heatmap_game"
)

frequency = get_number_frequency(game)

if frequency is None or frequency.empty:
    st.warning("No data available for this game.")
    st.stop()

fig = px.bar(
    frequency,
    x="Number",
    y="Times Drawn",
    title=f"{game} Number Frequency",
    labels={
        "Number": "Lottery Number",
        "Times Drawn": "Times Drawn"
    }
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("🔥 Top 10 Hot Numbers")

st.dataframe(
    frequency.sort_values(
        "Times Drawn",
        ascending=False
    ).head(10),
    width="stretch"
)