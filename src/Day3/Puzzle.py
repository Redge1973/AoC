import math
import string


class Stars:
    def __init__(self):
        self.stars = []

    def append(self, star):
        if not star in self.stars:
            self.stars.append(star)

    def __str__(self):
        return ';'.join([s.__str__() for s in self.stars])


class Star:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def __eq__(self, other):
        return self.column == other.column and self.row == other.row

    def __str__(self):
        return f'row:{self.row}:column:{self.column}'

    def __hash__(self):
        return hash(self.__str__())

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
        specialCharFound = False

        for currentCharIndex, currentChar in enumerate(line):

            if not currentChar.isdigit():
                continue
            digits.append(currentChar)

            specialCharFound = searchForSpecialcurrentCharactersInNeighbourhood(currentCharIndex, line, fileData, lineIndex,
                                                                         specialCharFound, Stars())

            nextcurrentChar = line[currentCharIndex+1] if currentCharIndex < len(line)-1 else None
            if not nextcurrentChar or not nextcurrentChar.isdigit():
                if specialCharFound and digits:
                    number = int(''.join(d for d in digits))
                    numbers.append(number)

                digits = []
                specialCharFound = False
    return sum(numbers, 0)



def findNumbersThatAreAdjacentToSymbolsAndStars(filepath):
    fileData = parseFile(filepath)

    numbers = []

    for lineIndex, line in enumerate(fileData):
        digits = []
        specialCharFound = False
        starsFound = Stars()

        for currentCharIndex, currentChar in enumerate(line):

            if not currentChar.isdigit():
                continue
            digits.append(currentChar)

            specialCharFound = searchForSpecialcurrentCharactersInNeighbourhood(currentCharIndex, line, fileData, lineIndex,
                                                                         specialCharFound, starsFound)

            nextcurrentChar = line[currentCharIndex+1] if currentCharIndex < len(line)-1 else None
            if not nextcurrentChar or not nextcurrentChar.isdigit():
                if specialCharFound and digits:
                    number = int(''.join(d for d in digits))
                    numbers.append({'number': number, 'stars': starsFound if starsFound.stars else None})

                digits = []
                specialCharFound = False
                starsFound = Stars()

    numbersWithStars = [n for n in numbers if n['stars']]

    starWithNumbers = findNumbersWithSameStars(numbersWithStars)

    result = 0
    for listOfNumbers in starWithNumbers.values():
        if len(listOfNumbers) > 1:
            result += math.prod(listOfNumbers)

    return result


def findNumbersWithSameStars(numbersWithStars):

    starWithNumbers = {}

    for n in numbersWithStars:
        number = n['number']
        for s in n['stars'].stars:
            if not starWithNumbers.get(s, None):
                starWithNumbers[s] = [number]
            else:
                starWithNumbers[s].append(number)

    return starWithNumbers






def searchForSpecialcurrentCharactersInNeighbourhood(currentCharIndex, line, fileData, lineIndex, specialCharFound, starsFound):
    star = '*'
    # check above
    if lineIndex > 0:
        char = fileData[lineIndex - 1][currentCharIndex]
        if char in specialcurrentCharsWithoutDot:
            if char == star:
                starsFound.append(Star(lineIndex-1, currentCharIndex))
            specialCharFound = True
    # check below
    if lineIndex < len(fileData) - 1:
        char = fileData[lineIndex + 1][currentCharIndex]
        if char in specialcurrentCharsWithoutDot:
            if char == star:
                starsFound.append(Star(lineIndex+1, currentCharIndex))
            specialCharFound = True
    if currentCharIndex > 0:
        # check above number and left
        if lineIndex > 0:
            char = fileData[lineIndex - 1][currentCharIndex - 1]
            if char in specialcurrentCharsWithoutDot:
                if char == star:
                    starsFound.append(Star(lineIndex-1, currentCharIndex-1))
                specialCharFound = True
        # check left from number
        char = line[currentCharIndex - 1]
        if char in specialcurrentCharsWithoutDot:
            if char == star:
                starsFound.append(Star(lineIndex, currentCharIndex-1))
            specialCharFound = True

        # check left and lower
        if lineIndex < len(fileData) - 1:
            char = fileData[lineIndex + 1][currentCharIndex - 1]
            if char in specialcurrentCharsWithoutDot:
                if char == star:
                    starsFound.append(Star(lineIndex+1, currentCharIndex-1))
                specialCharFound = True
    if currentCharIndex < len(line) - 1:
        # check above and right
        if lineIndex > 0:
            char = fileData[lineIndex - 1][currentCharIndex + 1]
            if char in specialcurrentCharsWithoutDot:
                if char == star:
                    starsFound.append(Star(lineIndex-1, currentCharIndex+1))
                specialCharFound = True

        # check right from number
        char = line[currentCharIndex + 1]
        if char in specialcurrentCharsWithoutDot:
            if char == star:
                starsFound.append(Star(lineIndex, currentCharIndex+1))
            specialCharFound = True

        # check right and lower
        if lineIndex < len(fileData) - 1:
            char = fileData[lineIndex + 1][currentCharIndex + 1]
            if char in specialcurrentCharsWithoutDot:
                if char == star:
                    starsFound.append(Star(lineIndex+1, currentCharIndex+1))
                specialCharFound = True
    return specialCharFound


