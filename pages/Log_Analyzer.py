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
    c2.metric("Unique IPs", len(set(ips)))
    c3.metric("Failed Events", len(failed_lines))
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

    st.subheader("🌐 Top IP Addresses")

    if ips:
        ip_df = pd.DataFrame(
            Counter(ips).most_common(10),
            columns=["IP Address", "Count"]
        )
        st.dataframe(ip_df, width="stretch")
        st.bar_chart(ip_df.set_index("IP Address"))
    else:
        st.info("No IP addresses found.")

    st.divider()

    st.subheader("🔎 Suspicious Keyword Counts")

    keyword_list = failed_keywords + warning_keywords + error_keywords + ioc_keywords

    keyword_df = pd.DataFrame(
        {
            "Keyword": keyword_list,
            "Count": [content.lower().count(word) for word in keyword_list]
        }
    ).sort_values("Count", ascending=False)

    st.dataframe(keyword_df, width="stretch")

    st.divider()

    st.subheader("🛡 Potential Indicators of Compromise")

    if ioc_hits:
        st.error(f"{len(ioc_hits)} possible IOC keyword match(es) detected.")
        st.dataframe(pd.DataFrame(ioc_hits, columns=["IOC Match"]), width="stretch")
    else:
        st.success("No IOC keywords detected.")

    st.divider()

    st.subheader("📊 Event Summary")

    summary_df = pd.DataFrame({
        "Category": ["Failed", "Warnings", "Errors", "IOC Hits"],
        "Count": [len(failed_lines), len(warning_lines), len(error_lines), len(ioc_hits)]
    })

    st.dataframe(summary_df, width="stretch")
    st.bar_chart(summary_df.set_index("Category"))

    st.divider()

    st.subheader("📤 Export Suspicious Events")

    suspicious_events = failed_lines + warning_lines + error_lines + ioc_hits

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

    st.subheader("📝 Incident Summary")

    incident_summary = f"""
SOC INCIDENT SUMMARY

Threat Level: {severity}
Suspicion Score: {suspicion_score}

Total Lines: {len(lines)}
Unique IP Addresses: {len(set(ips))}
Failed Events: {len(failed_lines)}
Warnings: {len(warning_lines)}
Errors: {len(error_lines)}
IOC Matches: {len(ioc_hits)}

Recommendation:
"""

    if suspicion_score >= 100:
        incident_summary += "Immediate investigation recommended. Review IOC matches and isolate affected systems."
    elif suspicion_score >= 50:
        incident_summary += "High-risk activity detected. Review authentication attempts and suspicious IP addresses."
    elif suspicion_score >= 20:
        incident_summary += "Moderate suspicious activity detected. Continue monitoring."
    else:
        incident_summary += "No significant indicators detected."

    st.text_area("Generated Report", incident_summary, height=260)

    st.download_button(
        label="Download Incident Report",
        data=incident_summary,
        file_name="oracle_incident_report.txt",
        mime="text/plain"
    )

    st.divider()

    st.subheader("👀 Log Preview")
    st.text("\n".join(lines[:50]))

else:
    st.info("Upload a log file to begin analysis.")

show_footer()