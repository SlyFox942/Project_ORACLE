import streamlit as st
import pandas as pd

from analysis.mitre_mapping import MITRE_MAP
from components.footer import show_footer

st.set_page_config(
    page_title="Threat Dashboard",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ ORACLE Threat Dashboard")
st.caption("Cybersecurity Overview")

# -----------------------
# Summary Metrics
# -----------------------

c1, c2, c3, c4 = st.columns(4)

c1.metric("IOC Rules", len(MITRE_MAP))
c2.metric("Threat Level", "🟢 Ready")
c3.metric("MITRE Techniques", len(set(
    item["technique"] for item in MITRE_MAP.values()
)))
c4.metric("Supported Tools", len(MITRE_MAP))

st.divider()

# -----------------------
# MITRE Table
# -----------------------

st.subheader("🎯 MITRE ATT&CK Techniques")

df = pd.DataFrame([
    {
        "Keyword": keyword,
        "Technique": value["technique"],
        "Technique Name": value["name"],
        "Tactic": value["tactic"]
    }
    for keyword, value in MITRE_MAP.items()
])

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

st.divider()

# -----------------------
# ATT&CK Tactics
# -----------------------

st.subheader("📊 ATT&CK Tactic Distribution")

chart = (
    df["Tactic"]
    .value_counts()
    .reset_index()
)

chart.columns = ["Tactic", "Count"]

st.bar_chart(
    chart.set_index("Tactic")
)

st.divider()

# -----------------------
# Roadmap
# -----------------------

st.subheader("🚀 Upcoming Threat Intelligence Features")

st.checkbox("VirusTotal Integration", disabled=True)
st.checkbox("AbuseIPDB Lookup", disabled=True)
st.checkbox("CVE Search", disabled=True)
st.checkbox("YARA Rule Scanner", disabled=True)
st.checkbox("Sigma Rule Detection", disabled=True)

show_footer()