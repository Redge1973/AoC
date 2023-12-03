import unittest

from src.Day3.Puzzle import parseFile, \
    findNumbersThatAreAdjacentToSymbols


class TestPuzzle(unittest.TestCase):

    def test_parseFile(self):
        result = parseFile('testInput2.txt')

        expectedResult =\
            [['4', '6', '7', '.', '.', '1', '1', '4', '.', '.'],
             ['.', '.', '.', '*', '.', '.', '.', '.', '.', '.']]
        self.assertEqual(result, expectedResult)

    def test_findNumbersThatAreAdjacentToSymbols(self):
        result = findNumbersThatAreAdjacentToSymbols('testInput2.txt')
        self.assertEqual(result, 467)

    def test_findNumbersThatAreAdjacentToSymbols2(self):
        result = findNumbersThatAreAdjacentToSymbols('testInput.txt')
        self.assertEqual(result, 4361)

    def test_findNumbersThatAreAdjacentToSymbols3(self):
        result = findNumbersThatAreAdjacentToSymbols('testInput3.txt')
        self.assertEqual(result, 692)



