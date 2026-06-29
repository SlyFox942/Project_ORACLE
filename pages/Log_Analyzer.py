import streamlit as st
import pandas as pd
import re
from collections import Counter

from components.footer import show_footer

st.title("📄 Log Analyzer")
st.caption("ORACLE Cyber Lab")

st.write(
    """
Upload a `.txt` or `.log` file and ORACLE will scan it for useful security signals,
including IP addresses, failed logins, errors, warnings, and suspicious keywords.
"""
)

uploaded_file = st.file_uploader("Upload log file", type=["txt", "log"])

if uploaded_file:
    content = uploaded_file.read().decode("utf-8", errors="ignore")
    lines = content.splitlines()

    st.subheader("📁 File Summary")
    st.metric("Total Lines", len(lines))
    st.metric("File Size", f"{len(content.encode('utf-8'))} bytes")

    ip_pattern = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
    ips = re.findall(ip_pattern, content)

    failed_keywords = ["failed", "failure", "invalid", "denied", "unauthorized"]
    warning_keywords = ["warning", "warn"]
    error_keywords = ["error", "critical", "fatal"]

    failed_lines = [
        line for line in lines
        if any(word in line.lower() for word in failed_keywords)
    ]

    warning_lines = [
        line for line in lines
        if any(word in line.lower() for word in warning_keywords)
    ]

    error_lines = [
        line for line in lines
        if any(word in line.lower() for word in error_keywords)
    ]

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("🌐 IP Addresses", len(set(ips)))
    c2.metric("🚫 Failed Events", len(failed_lines))
    c3.metric("⚠️ Warnings", len(warning_lines))
    c4.metric("🔥 Errors", len(error_lines))

    st.divider()

    st.subheader("🌐 Top IP Addresses")

    suspicion_score = (
        len(failed_lines) * 2
        + len(error_lines) * 3
        + len(warning_lines)
        + len(set(ips))
    )

    st.subheader("🚨 Suspicion Score")

    if suspicion_score >= 50:
        st.error(f"High suspicion score: {suspicion_score}")
    elif suspicion_score >= 20:
        st.warning(f"Medium suspicion score: {suspicion_score}")
    else:
        st.success(f"Low suspicion score: {suspicion_score}")
        
    if ips:
        ip_counts = Counter(ips)
        ip_df = pd.DataFrame(
            ip_counts.most_common(10),
            columns=["IP Address", "Count"]
        )
        st.dataframe(ip_df, width="stretch")
        st.bar_chart(ip_df.set_index("IP Address"))
    else:
        st.info("No IP addresses found.")

    st.divider()

    st.subheader("🚫 Failed / Suspicious Events")

    if failed_lines:
        st.dataframe(
            pd.DataFrame(failed_lines, columns=["Log Line"]),
            width="stretch"
        )
    else:
        st.success("No failed login or access-denied keywords found.")

    st.divider()

    st.subheader("🔥 Errors & Critical Events")

    if error_lines:
        st.dataframe(
            pd.DataFrame(error_lines, columns=["Log Line"]),
            width="stretch"
        )
    else:
        st.success("No error or critical keywords found.")

    st.divider()

    st.subheader("👀 Log Preview")

    st.text("\n".join(lines[:50]))

show_footer()