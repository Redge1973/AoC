import unittest

from src.Day4.Puzzle import parseFile, calculatePoints


class TestPuzzle(unittest.TestCase):

    def test_parseFile(self):
        result = parseFile('testInput1.txt')
        expectedResult = [{'numbers': ['83', '86', '6', '31', '17', '9', '48', '53'],
                           'winningNumbers': ['41', '48', '83', '86', '17']}]
        self.assertEqual(result, expectedResult)

    def test_calculatePoints(self):
        result = calculatePoints('testInput.txt')
        self.assertEqual(result, 13)
