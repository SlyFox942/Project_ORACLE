import streamlit as st
import sqlite3
import pandas as pd
from itertools import combinations
from collections import Counter

st.title("🎯 Pair Analysis")

game = st.selectbox("Choose Game", ["Mega Millions", "Powerball"])

conn = sqlite3.connect("data/oracle.db")
df = pd.read_sql_query(
    "SELECT * FROM drawings WHERE game = ?",
    conn,
    params=(game,)
)
conn.close()

if df.empty:
    st.warning("No data available for this game.")
    st.stop()

pair_counter = Counter()

for _, row in df.iterrows():
    numbers = [row["n1"], row["n2"], row["n3"], row["n4"], row["n5"]]
    for pair in combinations(sorted(numbers), 2):
        pair_counter[pair] += 1

pairs = []

for pair, count in pair_counter.most_common(20):
    pairs.append({
        "Pair": f"{pair[0]} + {pair[1]}",
        "Times Seen": count
    })

pair_df = pd.DataFrame(pairs)

st.subheader("Top 20 Most Common Pairs")
st.dataframe(pair_df, width="stretch")

st.bar_chart(pair_df.set_index("Pair"))