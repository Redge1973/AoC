import unittest

from src.Day2.Puzzle import findImpossibleGames, parseFile, calculateMaxPowerOfCubes


class TestPuzzle(unittest.TestCase):

    def test_parseFile(self):
        result = parseFile('testInput2.txt')

        expectedResult = \
            {'1': [[['3', 'blue'], ['4', 'red']],
                   [['1', 'red'], ['2', 'green'], ['6', 'blue']],
                   [['2', 'green']]]
             }
        self.assertEqual(result, expectedResult)

    def test_findImpossibleGames(self):
        result = findImpossibleGames('testInput.txt')
        self.assertEqual(result, 8)

    def test_calculateMaxPowerOfCubes(self):
        result = calculateMaxPowerOfCubes('testInput.txt')
        self.assertEqual(result, 2286)


