"""Test class"""
import unittest
import game

class FunctionTest(unittest.TestCase):
    """test class game"""

    def test_win(self):
        """case: win."""
        expected = 12
        result = game.Coin(1.0, 12, -10).play()
        self.assertEqual(expected, result)

    def test_lose(self):
        """case: lose."""
        expected = -10
        result = game.Coin(0.0, 12, -10).play()
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
