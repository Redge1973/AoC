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
    maxCubesPerColor = {'red': 12, 'green': 13, 'blue': 14}


    fileData = parseFile(filepath)

    for gameId, cubesList in fileData.items():
        valuesList = sum(cubesList, [])
        impossibleValueFound = False
        for v in valuesList:
            numberOfCubes = int(v[0])
            color = v[1]
            if numberOfCubes > maxCubesPerColor[color]:
                impossibleValueFound = True
                break
        if not impossibleValueFound:
            result += int(gameId)

    return result
