import streamlit as st
import sqlite3
import pandas as pd

DB = "data/oracle.db"

st.title("🩺 Database Health")

try:
    conn = sqlite3.connect(DB)

    df = pd.read_sql_query(
        "SELECT * FROM drawings",
        conn
    )

    conn.close()

except Exception as e:
    st.error(e)
    st.stop()

# ------------------------
# Metrics
# ------------------------

total = len(df)

duplicates = df.duplicated().sum()

missing = df.isnull().sum().sum()

date_min = df["draw_date"].min() if not df.empty else "N/A"
date_max = df["draw_date"].max() if not df.empty else "N/A"

c1, c2, c3, c4 = st.columns(4)

c1.metric("📊 Total Drawings", total)
c2.metric("📋 Duplicate Rows", duplicates)
c3.metric("⚠ Missing Values", missing)
c4.metric("📅 Date Range", f"{date_min} → {date_max}")

st.divider()

st.subheader("🎱 Game Counts")

st.dataframe(
    df["game"].value_counts().reset_index(
        name="Drawings"
    ),
    use_container_width=True
)

st.divider()

st.subheader("Recent Drawings")

st.dataframe(
    df.sort_values(
        "draw_date",
        ascending=False
    ),
    use_container_width=True
)