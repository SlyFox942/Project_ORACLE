import pandas as pd


def calculate_ai_score(data):

    if data is None:
        return pd.DataFrame()

    if isinstance(data, list):
        data = pd.DataFrame(data, columns=["Number", "Times Drawn"])

    if data.empty:
        return pd.DataFrame()

    results = []

    for _, row in data.iterrows():
        number = row["Number"]
        frequency = row["Times Drawn"]

        score = frequency * 0.70

        results.append({
            "Number": number,
            "Frequency": frequency,
            "AI Score": round(score, 2)
        })

    results = pd.DataFrame(results)

    return results.sort_values(
        by="AI Score",
        ascending=False
    )