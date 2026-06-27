import streamlit as st
from services.predictor import generate_balanced_pick

st.title("🎲 Experimental Pick Generator")

st.caption("For research and entertainment only. This does not predict winning numbers.")

game = st.selectbox("Choose Game", ["Mega Millions", "Powerball"])

if st.button("Generate ORACLE Pick"):
    pick, bonus = generate_balanced_pick(game)

    st.subheader("🔮 ORACLE Experimental Pick")

    st.write("White Balls:")
    st.header("  •  ".join(str(n) for n in pick))

    label = "Mega Ball" if game == "Mega Millions" else "Powerball"
    st.write(label)
    st.header(str(bonus))