import pandas as pd


class OracleEngine:

    def __init__(self, frequency_df):
        self.df = frequency_df.copy()

    def calculate_scores(self):

        if self.df.empty:
            return pd.DataFrame()

        max_frequency = self.df["Times Drawn"].max()

        self.df["Frequency Score"] = (
            self.df["Times Drawn"] / max_frequency
        ) * 100

        # These will become real calculations later
        self.df["Trend Score"] = 50
        self.df["Gap Score"] = 50
        self.df["Pair Score"] = 50

        self.df["Oracle Score"] = (
            self.df["Frequency Score"] * 0.40
            + self.df["Trend Score"] * 0.20
            + self.df["Gap Score"] * 0.20
            + self.df["Pair Score"] * 0.20
        ).round(2)

        return self.df.sort_values(
            "Oracle Score",
            ascending=False
        )