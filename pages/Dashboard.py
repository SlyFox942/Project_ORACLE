import streamlit as st
import sqlite3
import pandas as pd

st.title("🔮 Project ORACLE")

st.caption(
    "Lottery Analytics & Research Platform"
)

conn = sqlite3.connect("data/oracle.db")

try:

    df = pd.read_sql_query(
        "SELECT * FROM drawings",
        conn
    )

finally:
    conn.close()

total_drawings = len(df)

mega = len(df[df["game"] == "Mega Millions"])

power = len(df[df["game"] == "Powerball"])

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "📊 Total Drawings",
        total_drawings
    )

with col2:
    st.metric(
        "🎱 Mega Millions",
        mega
    )

with col3:
    st.metric(
        "🔴 Powerball",
        power
    )

st.divider()

st.subheader("Recent Drawings")

if df.empty:
    st.warning("No drawings imported.")
else:
    st.dataframe(
        df.sort_values(
            "draw_date",
            ascending=False
        ),
        width="stretch"
    )