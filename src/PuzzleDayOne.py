import re


def calculatePuzzle(filepath):
    file = open(filepath, 'r')
    result = 0

    for line in file:
        integers = []
        for c in line:
            if c.isdigit():
                integers.append(c)
        number = int(f'{integers[0]}{integers[len(integers) - 1]}')
        result += number
    file.close()
    return result


validStrings = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}
pattern = '|'.join(map(re.escape, validStrings.keys()))
regex = re.compile(fr'(?=({pattern}))')

def searchStrings(input):
    found = []
    matches = regex.finditer(input)
    for match in matches:
        match_value = match.group(1)
        if match_value:
            found.append(validStrings[match_value])
    return found

def calculatePuzzlePart2(filePath):
    file = open(filePath, 'r')
    result = 0

    for line in file:
        integers = searchStrings(line)
        number = int(f'{integers[0]}{integers[len(integers) - 1]}')
        result += number
    file.close()
    return result
