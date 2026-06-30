import streamlit as st
import pandas as pd

from analysis.mitre_mapping import MITRE_MAP
from components.footer import show_footer

st.title("🎯 MITRE ATT&CK Explorer")
st.caption("ORACLE Cyber Lab")

df = pd.DataFrame([
    {
        "Keyword": keyword,
        "Technique": details["technique"],
        "Technique Name": details["name"],
        "Tactic": details["tactic"]
    }
    for keyword, details in MITRE_MAP.items()
])

search = st.text_input("Search keyword, technique, or tactic")

if search:
    search_lower = search.lower()
    df = df[
        df.apply(
            lambda row: search_lower in " ".join(row.astype(str)).lower(),
            axis=1
        )
    ]

st.dataframe(df, width="stretch", hide_index=True)

show_footer()