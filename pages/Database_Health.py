import streamlit as st

from database.database_manager import DatabaseManager
from components.footer import show_footer

st.title("🩺 Database Health")

df = DatabaseManager.query("SELECT * FROM drawings")

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

if df.empty:
    st.warning("Database is empty.")
    show_footer()
    st.stop()

st.subheader("🎱 Game Counts")
st.dataframe(
    df["game"].value_counts().reset_index(name="Drawings"),
    width="stretch"
)

st.divider()

st.subheader("Recent Drawings")
st.dataframe(
    df.sort_values("draw_date", ascending=False),
    width="stretch"
)

show_footer()