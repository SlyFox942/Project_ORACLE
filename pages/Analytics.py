import streamlit as st
import pandas as pd
import plotly.express as px
from database.db import get_all_drawings

st.title("📊 ORACLE Analytics")

drawings = get_all_drawings()

if not drawings:
    st.warning("No drawings found. Import data first.")
    st.stop()

records = []

for row in drawings:
    game, draw_date, n1, n2, n3, n4, n5, bonus = row

    for number in [n1, n2, n3, n4, n5]:
        records.append({
            "Game": game,
            "Number": number
        })

df = pd.DataFrame(records)

game = st.selectbox(
    "Choose Lottery",
    sorted(df["Game"].unique())
)

filtered = df[df["Game"] == game]

frequency = (
    filtered["Number"]
    .value_counts()
    .sort_index()
    .reset_index()
)

frequency.columns = ["Number", "Times Drawn"]

# Summary Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Drawn Numbers", len(filtered))

with col2:
    st.metric("Unique Numbers", filtered["Number"].nunique())

with col3:
    hottest = frequency.sort_values("Times Drawn", ascending=False).iloc[0]
    st.metric(
        "🔥 Hottest Number",
        f'{int(hottest["Number"])} ({int(hottest["Times Drawn"])})'
    )

st.divider()

fig = px.bar(
    frequency,
    x="Number",
    y="Times Drawn",
    title=f"{game} Number Frequency"
)

st.plotly_chart(fig, use_container_width=True)