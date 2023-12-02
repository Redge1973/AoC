import unittest

from src.Day2.Puzzle import calculatePuzzle


class TestPuzzle(unittest.TestCase):

    def test_puzzlePart1(self):
        result = calculatePuzzle('testInputPuzzle1.txt')
        self.assertEqual(result, 0)

