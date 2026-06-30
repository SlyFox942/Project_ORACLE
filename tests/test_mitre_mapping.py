from analysis.mitre_mapping import MITRE_MAP


def test_mitre_map_contains_powershell():
    assert "powershell" in MITRE_MAP
    assert MITRE_MAP["powershell"]["technique"] == "T1059.001"


def test_mitre_map_entries_have_required_fields():
    for keyword, details in MITRE_MAP.items():
        assert "technique" in details
        assert "name" in details
        assert "tactic" in details