import streamlit as st

st.title("🛣️ ORACLE Roadmap")

tasks = {
    "Version 1.2": [
        "✅ Database Explorer",
        "✅ AI Rankings",
        "🔄 Command Center",
        "⬜ Heat Maps",
        "⬜ Trend Analysis",
        "⬜ Pair Analysis"
    ],
    "Version 2.0": [
        "⬜ Strategy Lab",
        "⬜ Monte Carlo",
        "⬜ AI Research",
        "⬜ Full Historical Data",
        "⬜ Export Reports"
    ]
}

for version, items in tasks.items():
    st.subheader(version)
    for item in items:
        st.write(item)