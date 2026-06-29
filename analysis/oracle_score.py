from analysis.frequency import get_number_frequency


def get_oracle_scores(game_name):
    frequency = get_number_frequency(game_name)

    if frequency is None or frequency.empty:
        return []

    max_count = frequency["Times Drawn"].max()

    scores = []

    for _, row in frequency.iterrows():

        number = int(row["Number"])
        count = int(row["Times Drawn"])

        frequency_score = (count / max_count) * 100

        scores.append({
            "Number": number,
            "Frequency": count,
            "Oracle Score": round(frequency_score, 2)
        })

    scores.sort(
        key=lambda x: x["Oracle Score"],
        reverse=True
    )

    return scores