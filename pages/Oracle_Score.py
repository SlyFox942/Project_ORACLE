import streamlit as st
import pandas as pd
import plotly.express as px
from analysis.oracle_score import get_oracle_scores

st.title("🔮 ORACLE Score")

st.caption("Experimental score for research and entertainment only.")

game = st.selectbox("Choose Game", ["Mega Millions", "Powerball"])

scores = get_oracle_scores(game)

if scores:
    df = pd.DataFrame(scores)

    st.dataframe(df, width="stretch")

    fig = px.bar(
        df,
        x="Number",
        y="Oracle Score",
        title=f"{game} ORACLE Score"
    )

    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("No data found yet.")