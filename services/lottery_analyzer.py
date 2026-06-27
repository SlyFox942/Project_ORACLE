from collections import Counter
from database.db import get_all_drawings


class LotteryAnalyzer:

    def __init__(self):
        self.drawings = get_all_drawings()

    def get_game_drawings(self, game):
        return [
            row for row in self.drawings
            if row[0] == game
        ]

    def frequency(self, game):

        numbers = []

        for row in self.get_game_drawings(game):

            numbers.extend(row[2:7])

        return Counter(numbers)

    def hot_numbers(self, game, limit=10):

        return self.frequency(game).most_common(limit)

    def cold_numbers(self, game, limit=10):

        counter = self.frequency(game)

        all_numbers = range(1, 71)

        missing = []

        for number in all_numbers:

            missing.append(
                (
                    number,
                    counter[number]
                )
            )

        return sorted(
            missing,
            key=lambda x: x[1]
        )[:limit]