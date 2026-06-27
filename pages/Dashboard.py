import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

DB = "data/oracle.db"

st.set_page_config(
    page_title="Project ORACLE",
    page_icon="🔮",
    layout="wide"
)

st.title("🔮 Project ORACLE")
st.caption("Lottery Analytics & Research Platform")

# -----------------------------
# Load Database
# -----------------------------
conn = sqlite3.connect(DB)
df = pd.read_sql_query("SELECT * FROM drawings", conn)
conn.close()

# -----------------------------
# Metrics
# -----------------------------
total = len(df)
mega = len(df[df["game"] == "Mega Millions"])
power = len(df[df["game"] == "Powerball"])

col1, col2, col3, col4 = st.columns(4)

col1.metric("📊 Total Drawings", total)
col2.metric("🎱 Mega Millions", mega)
col3.metric("🔴 Powerball", power)
col4.metric("🟢 Database", "Connected")

st.divider()

# -----------------------------
# Charts
# -----------------------------
if not df.empty:

    numbers = pd.concat([
        df["n1"],
        df["n2"],
        df["n3"],
        df["n4"],
        df["n5"]
    ])

    frequency = (
        numbers.value_counts()
        .sort_index()
        .reset_index()
    )

    frequency.columns = ["Number", "Times Drawn"]

    left, right = st.columns([2,1])

    with left:

        fig = px.bar(
            frequency,
            x="Number",
            y="Times Drawn",
            title="📈 Number Frequency"
        )

        st.plotly_chart(fig, use_container_width=True)

    with right:

        st.subheader("🔥 Top 10 Hot Numbers")

        st.dataframe(
            frequency.sort_values(
                "Times Drawn",
                ascending=False
            ).head(10),
            height=360,
            use_container_width=True
        )

    st.divider()

    st.subheader("📅 Latest Drawings")

    st.dataframe(
        df.sort_values(
            "draw_date",
            ascending=False
        ),
        use_container_width=True
    )

else:

    st.warning("Database is empty.")