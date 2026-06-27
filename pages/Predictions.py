import streamlit as st

from services.predictor import generate_balanced_pick
from services.oracle_ai import calculate_ai_score
from analysis.frequency import get_number_frequency

st.title("🎲 Experimental Pick Generator")

st.caption(
    "For research and entertainment only. "
    "This does not predict winning numbers."
)

game = st.selectbox(
    "Choose Game",
    ["Mega Millions", "Powerball"]
)

if st.button("Generate ORACLE Pick"):

    pick, bonus = generate_balanced_pick(game)

    # Get real frequency data
    frequency = get_number_frequency(game)

    # Calculate AI scores
    scores = calculate_ai_score(frequency)

    st.subheader("🧠 ORACLE AI Rankings")

    st.dataframe(
        scores.head(15),
        width="stretch"
    )

    st.subheader("🔮 ORACLE Experimental Pick")

    st.write("White Balls:")

    st.header(" • ".join(str(n) for n in pick))

    label = "Mega Ball" if game == "Mega Millions" else "Powerball"

    st.write(label)

    st.header(str(bonus))