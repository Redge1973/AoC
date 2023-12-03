import string
from functools import reduce


def parseFile(filepath):
    fileData = []

    file = open(filepath, 'r')

    for line in file:
        fileData.append([*line.strip()])

    file.close()

    return fileData


specialcurrentCharsWithoutDot = string.punctuation.replace('.', '')


def findNumbersThatAreAdjacentToSymbols(filepath):
    fileData = parseFile(filepath)

    numbers = []

    for lineIndex, line in enumerate(fileData):
        digits = []
        specialcurrentCharFound = False


        for currentCharIndex, currentChar in enumerate(line):

            if not currentChar.isdigit():
                continue
            digits.append(currentChar)

            specialcurrentCharFound = searchForSpecialcurrentCharactersInNeighbourhood(currentCharIndex, line, fileData, lineIndex,
                                                                         specialcurrentCharFound)

            nextcurrentChar = line[currentCharIndex+1] if currentCharIndex < len(line)-1 else None
            if not nextcurrentChar or not nextcurrentChar.isdigit():
                if specialcurrentCharFound and digits:
                    number = int(''.join(d for d in digits))
                    numbers.append(number)

                digits = []
                specialcurrentCharFound = False


    return sum(numbers, 0)


def searchForSpecialcurrentCharactersInNeighbourhood(currentCharIndex, line, fileData, lineIndex, specialcurrentCharFound):
    # check above
    if lineIndex > 0:
        if fileData[lineIndex - 1][currentCharIndex] in specialcurrentCharsWithoutDot:
            specialcurrentCharFound = True
    # check below
    if lineIndex < len(fileData) - 1:
        if fileData[lineIndex + 1][currentCharIndex] in specialcurrentCharsWithoutDot:
            specialcurrentCharFound = True
    if currentCharIndex > 0:
        # check above number and left
        if lineIndex > 0:
            if fileData[lineIndex - 1][currentCharIndex - 1] in specialcurrentCharsWithoutDot:
                specialcurrentCharFound = True
        # check left from number
        if line[currentCharIndex - 1] in specialcurrentCharsWithoutDot:
            specialcurrentCharFound = True

        # check left and lower
        if lineIndex < len(fileData) - 1:
            if fileData[lineIndex + 1][currentCharIndex - 1] in specialcurrentCharsWithoutDot:
                specialcurrentCharFound = True
    if currentCharIndex < len(line) - 1:
        # check above and right
        if lineIndex > 0:
            if fileData[lineIndex - 1][currentCharIndex + 1] in specialcurrentCharsWithoutDot:
                specialcurrentCharFound = True

        # check right from number
        if line[currentCharIndex + 1] in specialcurrentCharsWithoutDot:
            specialcurrentCharFound = True

        # check right and lower
        if lineIndex < len(fileData) - 1:
            if fileData[lineIndex + 1][currentCharIndex + 1] in specialcurrentCharsWithoutDot:
                specialcurrentCharFound = True
    return specialcurrentCharFound


