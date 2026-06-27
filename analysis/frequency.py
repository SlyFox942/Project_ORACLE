from collections import Counter
from database.db import get_all_drawings

def get_number_frequency(game_name):
    drawings = get_all_drawings()
    counter = Counter()

    for row in drawings:
        game, draw_date, n1, n2, n3, n4, n5, bonus = row

        if game == game_name:
            counter.update([n1, n2, n3, n4, n5])

    return counter.most_common()