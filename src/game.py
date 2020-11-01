"""Game class"""
import random


class Coin:
    """Coin Game"""
    def __init__(self, win_rate, win_profit, lose_profit):
        """parameter of game."""
        self.win_rate = float(win_rate)
        self.win_profit = float(win_profit)
        self.lose_profit = float(lose_profit)

    def play(self):
        """Star."""
        if random.random() < self.win_rate:
            return self.win_profit

        return self.lose_profit

    @property
    def return_win_rate(self):
        """parameter of game."""
        return self.win_rate

    @property
    def return_win_profit(self):
        """parameter of game."""
        return self.win_profit

    @property
    def reture_lose_profit(self):
        """parameter of game."""
        return self.lose_profit
