"""
.. module:: main
    :synopsis:A simple module for coin game

.. moduleauthor:: Wei-Yu
"""
from game import Coin

i = int(input('number of times:'))

play_game = Coin(0.5, 12, -10)
PROFIT = 0.0

for j in range(i):
    PROFIT = PROFIT + play_game.play()

print('profit:', PROFIT)
