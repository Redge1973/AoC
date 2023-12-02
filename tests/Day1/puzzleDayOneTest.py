import unittest

from src.Day1.PuzzleDayOne import calculatePuzzlePart2, calculatePuzzle


class TestPuzzleDayOne(unittest.TestCase):

    def test_puzzlePart1(self):
        result = calculatePuzzle('testInputPuzzle1.txt')
        self.assertEqual(result, 142)


    def test_puzzlePart2(self):
        result = calculatePuzzlePart2('testInput.txt')
        self.assertEqual(result, 281)

    def test_puzzlePart21(self):
        result = calculatePuzzlePart2('testInput2.txt')
        self.assertEqual(result, 11+12+21)

    def test_puzzlePart22(self):
        result = calculatePuzzlePart2('testInput3.txt')
        self.assertEqual(result, 68)
