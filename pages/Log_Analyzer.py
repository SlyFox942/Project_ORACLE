import streamlit as st
import pandas as pd
import re
from collections import Counter

from components.footer import show_footer

st.title("📄 SOC Log Analyzer")
st.caption("ORACLE Cyber Lab")

st.write(
    """
Upload a `.txt` or `.log` file and ORACLE will scan it for useful security signals,
including IP addresses, failed logins, errors, warnings, suspicious keywords,
and possible indicators of compromise.
"""
)

uploaded_file = st.file_uploader("Upload log file", type=["txt", "log"])

if uploaded_file:
    content = uploaded_file.read().decode("utf-8", errors="ignore")
    lines = content.splitlines()

    ip_pattern = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
    ips = re.findall(ip_pattern, content)

    failed_keywords = ["failed", "failure", "invalid", "denied", "unauthorized"]
    warning_keywords = ["warning", "warn"]
    error_keywords = ["error", "critical", "fatal"]
    ioc_keywords = [
        "powershell", "cmd.exe", "mimikatz", "psexec", "rundll32",
        "regsvr32", "wget", "curl", "nc.exe", "certutil"
    ]

    failed_lines = [line for line in lines if any(word in line.lower() for word in failed_keywords)]
    warning_lines = [line for line in lines if any(word in line.lower() for word in warning_keywords)]
    error_lines = [line for line in lines if any(word in line.lower() for word in error_keywords)]
    ioc_hits = [line for line in lines if any(word in line.lower() for word in ioc_keywords)]

    st.subheader("📁 File Summary")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Lines", len(lines))
    c2.metric("File Size", f"{len(content.encode('utf-8'))} bytes")
    c3.metric("Unique IPs", len(set(ips)))
    c4.metric("IOC Hits", len(ioc_hits))

    st.divider()

    suspicion_score = (
        len(failed_lines) * 2
        + len(error_lines) * 3
        + len(warning_lines)
        + len(set(ips))
        + len(ioc_hits) * 5
    )

    st.subheader("🚨 Suspicion Score")

    if suspicion_score >= 100:
        severity = "🔴 Critical"
        st.error(f"{severity} — Score: {suspicion_score}")
    elif suspicion_score >= 50:
        severity = "🟠 High"
        st.error(f"{severity} — Score: {suspicion_score}")
    elif suspicion_score >= 20:
        severity = "🟡 Medium"
        st.warning(f"{severity} — Score: {suspicion_score}")
    else:
        severity = "🟢 Low"
        st.success(f"{severity} — Score: {suspicion_score}")

    st.divider()

    st.subheader("📊 Log Severity Breakdown")

    severity_rows = []

    for line in lines:
        lower_line = line.lower()

        if any(word in lower_line for word in error_keywords):
            severity_label = "Error / Critical"
        elif any(word in lower_line for word in failed_keywords):
            severity_label = "Failed / Suspicious"
        elif any(word in lower_line for word in warning_keywords):
            severity_label = "Warning"
        else:
            severity_label = "Informational"

        severity_rows.append({
            "Severity": severity_label,
            "Log Line": line
        })

    severity_df = pd.DataFrame(severity_rows)
    severity_counts = severity_df["Severity"].value_counts().reset_index()
    severity_counts.columns = ["Severity", "Count"]

    st.dataframe(severity_counts, width="stretch")
    st.bar_chart(severity_counts.set_index("Severity"))

    st.divider()

    st.subheader("🌐 Top IP Addresses")

    if ips:
        ip_counts = Counter(ips)
        ip_df = pd.DataFrame(ip_counts.most_common(10), columns=["IP Address", "Count"])
        st.dataframe(ip_df, width="stretch")
        st.bar_chart(ip_df.set_index("IP Address"))
    else:
        st.info("No IP addresses found.")

    st.divider()

    st.subheader("🔎 Top Suspicious Keywords")

    keyword_list = failed_keywords + warning_keywords + error_keywords + ioc_keywords
    keyword_counts = {
        keyword: content.lower().count(keyword)
        for keyword in keyword_list
    }

    keyword_df = pd.DataFrame(keyword_counts.items(), columns=["Keyword", "Count"])
    keyword_df = keyword_df.sort_values("Count", ascending=False)

    st.dataframe(keyword_df, width="stretch")

    st.divider()

    st.subheader("🛡 Potential Indicators of Compromise")

    if ioc_hits:
        st.error(f"{len(ioc_hits)} possible IOC keyword match(es) detected.")
        st.dataframe(pd.DataFrame(ioc_hits, columns=["IOC Match"]), width="stretch")
    else:
        st.success("No IOC keywords detected.")

    st.divider()

    st.subheader("🚫 Failed / Suspicious Events")

    if failed_lines:
        st.dataframe(pd.DataFrame(failed_lines, columns=["Log Line"]), width="stretch")
    else:
        st.success("No failed login or access-denied keywords found.")

    st.divider()

    st.subheader("🔥 Errors & Critical Events")

    if error_lines:
        st.dataframe(pd.DataFrame(error_lines, columns=["Log Line"]), width="stretch")
    else:
        st.success("No error or critical keywords found.")

    st.divider()

    st.subheader("📤 Export Suspicious Events")

    suspicious_events = failed_lines + error_lines + warning_lines + ioc_hits

    if suspicious_events:
        export_df = pd.DataFrame(suspicious_events, columns=["Log Line"])
        csv_data = export_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="Download Suspicious Events CSV",
            data=csv_data,
            file_name="oracle_suspicious_events.csv",
            mime="text/csv"
        )
    else:
        st.info("No suspicious events available to export.")

    st.divider()

    st.subheader("👀 Log Preview")
    st.text("\n".join(lines[:50]))

else:
    st.info("Upload a log file to begin analysis.")

show_footer()