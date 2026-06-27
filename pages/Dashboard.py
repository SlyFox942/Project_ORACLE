import streamlit as st
from database.db import get_all_drawings

st.title("🔮 Project ORACLE")

drawings = get_all_drawings()

mega = len([d for d in drawings if d[0] == "Mega Millions"])
power = len([d for d in drawings if d[0] == "Powerball"])

c1, c2, c3 = st.columns(3)

c1.metric("📊 Total Drawings", len(drawings))
c2.metric("🎱 Mega Millions", mega)
c3.metric("🔴 Powerball", power)

st.divider()

st.subheader("Latest Database Records")

st.dataframe(drawings, width="stretch")