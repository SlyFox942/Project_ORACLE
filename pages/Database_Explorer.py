import streamlit as st
import sqlite3
import pandas as pd

DB_PATH = "data/oracle.db"

st.title("🗄️ Database Explorer")

try:
    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql_query(
        "SELECT * FROM drawings ORDER BY draw_date DESC",
        conn
    )

    conn.close()

    st.metric("Total Drawings", len(df))

    if df.empty:
        st.warning("Database is empty.")
        st.stop()

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Mega Millions", len(df[df["game"] == "Mega Millions"]))

    with col2:
        st.metric("Powerball", len(df[df["game"] == "Powerball"]))

    st.divider()

    st.subheader("Games in Database")
    st.write(df["game"].value_counts())

    st.divider()

    st.subheader("Latest Drawings")
    st.dataframe(df, width="stretch")

except Exception as e:
    st.error(e)