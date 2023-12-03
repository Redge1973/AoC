import string
from functools import reduce


def parseFile(filepath):
    fileData = []

    file = open(filepath, 'r')

    for line in file:
        fileData.append([*line.strip()])

    file.close()

    return fileData


specialCharsWithoutDot = string.punctuation.replace('.', '')


def findNumbersThatAreAdjacentToSymbols(filepath):
    fileData = parseFile(filepath)

    numbers = []

    for listIndex, charList in enumerate(fileData):
        digits = []
        specialCharFound = False

        print(f'Zeile {listIndex}:-------------------------------------------------')

        for charIndex, char in enumerate(charList):

            if not char.isdigit():
                continue
            digits.append(char)

            # check above
            if listIndex > 0:
                if fileData[listIndex - 1][charIndex] in specialCharsWithoutDot:
                    specialCharFound = True

            # check below
            if listIndex < len(fileData)-1:
                if fileData[listIndex + 1][charIndex] in specialCharsWithoutDot:
                    specialCharFound = True

            if charIndex > 0:
                # check above number and left
                if listIndex > 0:
                    if fileData[listIndex - 1][charIndex - 1] in specialCharsWithoutDot:
                        specialCharFound = True
                # check left from number
                if charList[charIndex - 1] in specialCharsWithoutDot:
                    specialCharFound = True

                #check left and lower
                if listIndex < len(fileData) -1:
                    if fileData[listIndex + 1][charIndex - 1] in specialCharsWithoutDot:
                        specialCharFound = True



            if charIndex < len(charList)-1:
                # check above and right
                if listIndex > 0:
                    if fileData[listIndex - 1][charIndex + 1] in specialCharsWithoutDot:
                        specialCharFound = True

                # check right from number
                if charList[charIndex + 1] in specialCharsWithoutDot:
                    specialCharFound = True

                # check right and lower
                if listIndex < len(fileData) - 1:
                    if fileData[listIndex + 1][charIndex + 1] in specialCharsWithoutDot:
                        specialCharFound = True

            nextChar = charList[charIndex+1] if charIndex < len(charList)-1 else None
            if not nextChar or not nextChar.isdigit():
                if specialCharFound and digits:
                    number = int(''.join(d for d in digits))
                    print(number)
                    numbers.append(number)

                digits = []
                specialCharFound = False


    return sum(numbers, 0)


