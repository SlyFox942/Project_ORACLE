import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

st.title("📈 Trend Analysis")

game = st.selectbox("Choose Game", ["Mega Millions", "Powerball"])

conn = sqlite3.connect("data/oracle.db")
df = pd.read_sql_query(
    "SELECT * FROM drawings WHERE game = ? ORDER BY draw_date",
    conn,
    params=(game,)
)
conn.close()

if df.empty:
    st.warning("No data available for this game.")
    st.stop()

number = st.number_input("Choose a number", min_value=1, max_value=70, value=1)

df["draw_date"] = pd.to_datetime(df["draw_date"])

matches = []

for _, row in df.iterrows():
    appeared = number in [row["n1"], row["n2"], row["n3"], row["n4"], row["n5"]]
    matches.append(1 if appeared else 0)

df["Appeared"] = matches
df["Rolling Hits"] = df["Appeared"].rolling(window=5, min_periods=1).sum()

fig = px.line(
    df,
    x="draw_date",
    y="Rolling Hits",
    title=f"Number {number} Trend for {game}"
)

st.plotly_chart(fig, use_container_width=True)

st.write("Draws containing this number:")
st.dataframe(df[df["Appeared"] == 1], width="stretch")