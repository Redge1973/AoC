from src.PuzzleDayOne import calculatePuzzlePart2, calculatePuzzle

if __name__ == '__main__':
    filepath = './src/input2.txt'
    result = calculatePuzzle(filepath)
    print(result)
    result = calculatePuzzlePart2(filepath)
    print(result)
