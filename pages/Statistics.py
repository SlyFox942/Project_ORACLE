import streamlit as st
import pandas as pd
import plotly.express as px
from analysis.frequency import get_number_frequency

st.title("📊 Lottery Statistics")

game = st.selectbox(
    "Select Lottery",
    ["Mega Millions", "Powerball"]
)

frequency = get_number_frequency(game)

if frequency:

    df = pd.DataFrame(
        frequency,
        columns=["Number", "Times Drawn"]
    )

    st.subheader(f"🔥 Hot Numbers - {game}")

    st.dataframe(df, width="stretch")

    fig = px.bar(
        df,
        x="Number",
        y="Times Drawn",
        title="Winning Number Frequency"
    )

    st.plotly_chart(fig, width="stretch")

else:

    st.warning("No drawings found.")