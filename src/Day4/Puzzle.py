

def parseFile(filepath):
    fileData = []

    file = open(filepath, 'r')

    for line in file:
        n = line.split(':')[1].strip().split('|')

        winningNumbers = n[0].strip().split(' ')
        # filter out empty strings
        winningNumbers = [v for v in winningNumbers if v]
        numbers = n[1].split(' ')
        numbers = [v for v in numbers if v]
        fileData.append({'winningNumbers': winningNumbers, 'numbers': numbers})

    file.close()

    return fileData


def calculatePoints(filename):

    cards = parseFile(filename)

    result = 0
    for line in cards:
        print(line)
        winningNumbers = line['winningNumbers']
        numbers = line['numbers']

        numberOfMatches = len(list(set(winningNumbers).intersection(numbers)))
        points = int(2**(numberOfMatches - 1))
        result += points

    return result

