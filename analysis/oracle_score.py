from analysis.frequency import get_number_frequency


def get_oracle_scores(game_name):
    frequency = get_number_frequency(game_name)

    if not frequency:
        return []

    max_count = max(count for number, count in frequency)

    scores = []

    for number, count in frequency:
        frequency_score = (count / max_count) * 100

        scores.append({
            "Number": number,
            "Frequency": count,
            "Oracle Score": round(frequency_score, 2)
        })

    return sorted(scores, key=lambda x: x["Oracle Score"], reverse=True)