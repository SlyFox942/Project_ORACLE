import streamlit as st
import pandas as pd
import re
from collections import Counter

from components.footer import show_footer
from analysis.mitre_mapping import MITRE_MAP

st.title("📄 SOC Log Analyzer")
st.caption("ORACLE Cyber Lab")

st.write(
    """
Upload a `.txt` or `.log` file and ORACLE will scan it for useful security signals,
including IP addresses, failed logins, errors, warnings, suspicious keywords,
possible indicators of compromise, and MITRE ATT&CK matches.
"""
)

uploaded_file = st.file_uploader("Upload log file", type=["txt", "log"])


def extract_ip_addresses(text):
    ip_pattern = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
    return re.findall(ip_pattern, text)


def find_matching_lines(lines, keywords):
    return [
        line for line in lines
        if any(keyword in line.lower() for keyword in keywords)
    ]


def calculate_suspicion_score(failed, warnings, errors, unique_ips, iocs):
    return (
        len(failed) * 2
        + len(errors) * 3
        + len(warnings)
        + unique_ips
        + len(iocs) * 5
    )


def get_threat_level(score):
    if score >= 100:
        return "🔴 Critical"
    elif score >= 50:
        return "🟠 High"
    elif score >= 20:
        return "🟡 Medium"
    else:
        return "🟢 Low"


if uploaded_file:
    content = uploaded_file.read().decode("utf-8", errors="ignore")
    lines = content.splitlines()
    lower_content = content.lower()

    failed_keywords = ["failed", "failure", "invalid", "denied", "unauthorized"]
    warning_keywords = ["warning", "warn"]
    error_keywords = ["error", "critical", "fatal"]

    ioc_keywords = [
        "powershell",
        "cmd.exe",
        "mimikatz",
        "psexec",
        "rundll32",
        "regsvr32",
        "wget",
        "curl",
        "nc.exe",
        "certutil"
    ]

    ips = extract_ip_addresses(content)

    failed_lines = find_matching_lines(lines, failed_keywords)
    warning_lines = find_matching_lines(lines, warning_keywords)
    error_lines = find_matching_lines(lines, error_keywords)
    ioc_hits = find_matching_lines(lines, ioc_keywords)

    suspicion_score = calculate_suspicion_score(
        failed_lines,
        warning_lines,
        error_lines,
        len(set(ips)),
        ioc_hits
    )

    threat_level = get_threat_level(suspicion_score)

    st.subheader("📁 File Summary")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total Lines", len(lines))
    c2.metric("Unique IPs", len(set(ips)))
    c3.metric("Failed Events", len(failed_lines))
    c4.metric("IOC Hits", len(ioc_hits))

    st.divider()

    st.subheader("🚨 Suspicion Score")

    if suspicion_score >= 50:
        st.error(f"{threat_level} — Score: {suspicion_score}")
    elif suspicion_score >= 20:
        st.warning(f"{threat_level} — Score: {suspicion_score}")
    else:
        st.success(f"{threat_level} — Score: {suspicion_score}")

    st.divider()

    st.subheader("📊 Event Summary")

    summary_df = pd.DataFrame({
        "Category": ["Failed", "Warnings", "Errors", "IOC Hits"],
        "Count": [
            len(failed_lines),
            len(warning_lines),
            len(error_lines),
            len(ioc_hits)
        ]
    })

    st.dataframe(summary_df, width="stretch")
    st.bar_chart(summary_df.set_index("Category"))

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

    keyword_df = pd.DataFrame({
        "Keyword": keyword_list,
        "Count": [lower_content.count(keyword) for keyword in keyword_list]
    }).sort_values("Count", ascending=False)

    st.dataframe(keyword_df, width="stretch")

    st.divider()

    st.subheader("🛡 Potential Indicators of Compromise")

    if ioc_hits:
        st.error(f"{len(ioc_hits)} possible IOC keyword match(es) detected.")
        st.dataframe(
            pd.DataFrame(ioc_hits, columns=["IOC Match"]),
            width="stretch"
        )
    else:
        st.success("No IOC keywords detected.")

    st.divider()

    st.subheader("🎯 MITRE ATT&CK Mapping")

    mitre_matches = []

    for keyword, details in MITRE_MAP.items():
        if keyword in lower_content:
            mitre_matches.append({
                "Keyword": keyword,
                "Technique": details["technique"],
                "Technique Name": details["name"],
                "Tactic": details["tactic"]
            })

    if mitre_matches:
        st.dataframe(pd.DataFrame(mitre_matches), width="stretch")
    else:
        st.success("No MITRE ATT&CK techniques detected.")

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

Threat Level: {threat_level}
Suspicion Score: {suspicion_score}

Total Lines: {len(lines)}
Unique IP Addresses: {len(set(ips))}
Failed Events: {len(failed_lines)}
Warnings: {len(warning_lines)}
Errors: {len(error_lines)}
IOC Matches: {len(ioc_hits)}
MITRE Matches: {len(mitre_matches)}

Recommendation:
"""

    if suspicion_score >= 100:
        incident_summary += "Immediate investigation recommended. Review IOC matches, MITRE mappings, and isolate affected systems."
    elif suspicion_score >= 50:
        incident_summary += "High-risk activity detected. Review authentication attempts, suspicious IP addresses, and IOC matches."
    elif suspicion_score >= 20:
        incident_summary += "Moderate suspicious activity detected. Continue monitoring and review suspicious events."
    else:
        incident_summary += "No significant indicators detected."

    st.text_area(
        "Generated Report",
        incident_summary,
        height=280
    )

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