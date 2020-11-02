"""
.. module:: main
    :synopsis:A simple module for coin game

.. moduleauthor:: Wei-Yu
"""
import sys
from game import Coin

def main(i):
    """This is main."""
    play_game = Coin(0.5, 12, -10)
    lose_rate = 0.0

    for j in range(int(i[1])):
        if play_game.play()<0:
            lose_rate=lose_rate+1

    print('P_lose = ', lose_rate/(j+1))

if __name__ == "__main__":
    main(sys.argv)
