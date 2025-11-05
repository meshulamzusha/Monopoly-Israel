import random

class Dice:
    @staticmethod
    def rolling_dice() -> int:
        return random.randint(0, 6)