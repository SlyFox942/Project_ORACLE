import random


def generate_balanced_pick(game):
    if game == "Mega Millions":
        max_white = 70
        max_bonus = 24
    else:
        max_white = 69
        max_bonus = 26

    lows = list(range(1, 36))
    highs = list(range(36, max_white + 1))

    pick = random.sample(lows, 2) + random.sample(highs, 3)
    pick.sort()

    bonus = random.randint(1, max_bonus)

    return pick, bonus