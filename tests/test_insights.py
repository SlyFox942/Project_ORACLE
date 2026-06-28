import pandas as pd

from analysis.insights import generate_insights


def test_generate_insights():

    df = pd.DataFrame({
        "n1": [1, 5],
        "n2": [2, 6],
        "n3": [3, 7],
        "n4": [4, 8],
        "n5": [5, 9]
    })

    insights = generate_insights(df)

    assert insights is not None
    assert "hottest_number" in insights
    assert "coldest_number" in insights
    assert "average_draw_sum" in insights