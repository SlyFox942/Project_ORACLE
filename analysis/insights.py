import pandas as pd


def generate_insights(df):
    """Generate summary statistics from historical drawings."""

    if df.empty:
        return None

    numbers = pd.concat([
        df["n1"],
        df["n2"],
        df["n3"],
        df["n4"],
        df["n5"]
    ])

    frequency = numbers.value_counts()

    insights = {
        "total_drawings": len(df),
        "hottest_number": int(frequency.idxmax()),
        "coldest_number": int(frequency.idxmin()),
        "average_draw_sum": round(
            df[["n1", "n2", "n3", "n4", "n5"]]
            .sum(axis=1)
            .mean(),
            2
        ),
        "odd_numbers": int((numbers % 2 == 1).sum()),
        "even_numbers": int((numbers % 2 == 0).sum()),
    }

    return insights