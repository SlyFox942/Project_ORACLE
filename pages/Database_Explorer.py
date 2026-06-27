import streamlit as st

from database.database_manager import DatabaseManager
from components.footer import show_footer

st.title("🗄️ Database Explorer")

df = DatabaseManager.query(
    "SELECT * FROM drawings ORDER BY draw_date DESC"
)

st.metric("Total Drawings", len(df))

if df.empty:
    st.warning("Database is empty.")
    show_footer()
    st.stop()

col1, col2 = st.columns(2)

col1.metric("Mega Millions", len(df[df["game"] == "Mega Millions"]))
col2.metric("Powerball", len(df[df["game"] == "Powerball"]))

st.divider()

st.subheader("Games in Database")
st.write(df["game"].value_counts())

st.divider()

st.subheader("Latest Drawings")
st.dataframe(df, width="stretch")

show_footer()