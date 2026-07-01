import streamlit as st

from components.footer import show_footer
from analysis.mitre_mapping import MITRE_MAP

st.set_page_config(
    page_title="ORACLE Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 ORACLE Assistant")
st.caption("Cybersecurity & Analytics Knowledge Assistant")

question = st.text_input(
    "Ask ORACLE a question",
    placeholder="Example: What is PowerShell? What is T1059.001?"
)

if question:

    q = question.lower()

    answered = False

    for keyword, details in MITRE_MAP.items():

        if keyword in q:

            st.success(f"Keyword: {keyword}")

            st.markdown(f"**Technique:** {details['technique']}")
            st.markdown(f"**Name:** {details['name']}")
            st.markdown(f"**Tactic:** {details['tactic']}")

            answered = True

    if "t1059" in q:
        st.info("""
T1059 is MITRE ATT&CK's Command and Scripting Interpreter technique.

Attackers frequently use PowerShell or cmd.exe
to execute malicious commands.
""")
        answered = True

    if "hash" in q:
        st.info("""
Hashes uniquely identify files.

Common algorithms include:

• MD5
• SHA-1
• SHA-256

Hashes help verify file integrity.
""")
        answered = True

    if "ioc" in q:
        st.info("""
Indicators of Compromise (IOCs) include:

• IP addresses

• Domains

• File hashes

• Registry keys

• Process names

used to identify malicious activity.
""")
        answered = True

    if not answered:
        st.warning(
            "ORACLE doesn't know that yet. More knowledge will be added in future versions."
        )

show_footer()