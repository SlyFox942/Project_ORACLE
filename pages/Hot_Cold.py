import streamlit as st
import pandas as pd
from services.lottery_analyzer import LotteryAnalyzer

st.title("🔥❄️ Hot & Cold Numbers")

game = st.selectbox("Choose Game", ["Mega Millions", "Powerball"])

analyzer = LotteryAnalyzer()

hot = analyzer.hot_numbers(game, 10)
cold = analyzer.cold_numbers(game, 10)

col1, col2 = st.columns(2)

with col1:
    st.subheader("🔥 Hot Numbers")
    hot_df = pd.DataFrame(hot, columns=["Number", "Times Drawn"])
    st.dataframe(hot_df, width="stretch")
    st.bar_chart(hot_df.set_index("Number"))

with col2:
    st.subheader("❄️ Cold Numbers")
    cold_df = pd.DataFrame(cold, columns=["Number", "Times Drawn"])
    st.dataframe(cold_df, width="stretch")
    st.bar_chart(cold_df.set_index("Number"))