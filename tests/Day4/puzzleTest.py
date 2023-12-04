import unittest

from src.Day4.Puzzle import parseFile, calculatePoints


class TestPuzzle(unittest.TestCase):

    def test_parseFile(self):
        result = parseFile('testInput1.txt')
        expectedResult = "numbers:['41', '48', '83', '86', '17'] winningNumbers:['41', '48', '83', '86', '17']"
        self.assertEqual(result.__str__(), expectedResult)

    def test_calculatePoints(self):
        result = calculatePoints('testInput.txt')
        self.assertEqual(result, 13)

    def test_calculatePointsInputProd(self):
        result = calculatePoints('../../src/Day4/input.txt')
        self.assertEqual(result, 25571)
