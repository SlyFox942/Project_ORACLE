MITRE_MAP = {
    "powershell": {
        "technique": "T1059.001",
        "name": "PowerShell",
        "tactic": "Execution"
    },
    "cmd.exe": {
        "technique": "T1059.003",
        "name": "Windows Command Shell",
        "tactic": "Execution"
    },
    "certutil": {
        "technique": "T1105",
        "name": "Ingress Tool Transfer",
        "tactic": "Command and Control"
    },
    "psexec": {
        "technique": "T1021.002",
        "name": "SMB/Windows Admin Shares",
        "tactic": "Lateral Movement"
    },
    "mimikatz": {
        "technique": "T1003",
        "name": "Credential Dumping",
        "tactic": "Credential Access"
    },
    "curl": {
        "technique": "T1105",
        "name": "Ingress Tool Transfer",
        "tactic": "Command and Control"
    },
    "wget": {
        "technique": "T1105",
        "name": "Ingress Tool Transfer",
        "tactic": "Command and Control"
    }
}