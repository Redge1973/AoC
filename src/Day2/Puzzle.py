def parseFile(filepath):
    fileData = {}

    file = open(filepath, 'r')

    for line in file:
        v = line.split(':')
        gameId = v[0].strip().replace('Game ', '')
        results = []
        for r in [value.strip() for value in v[1].split(';')]:
            results.append([value.strip().split(' ') for value in r.split(',')])

        fileData[gameId] = results

    file.close()

    return fileData


def calculatePuzzle(filepath):
    result = 0
    red = 12
    green = 13
    blue = 14

    fileData = parseFile(filepath)

    for key, value in fileData.items():
        print(key)
        print(value)


    return result
