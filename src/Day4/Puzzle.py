

class Cards:

    def __init__(self):
        self.cards = []

    def append(self, card):
        self.cards.append(card)

    def __str__(self):
        return ' '.join([c.__str__() for c in self.cards])


class Card:
    def __init__(self, id, winningNumbers, numbers):
        self.id = id
        self.winningNumbers = winningNumbers
        self.numbers = numbers

    def __str__(self):
        return f'numbers:{self.winningNumbers} winningNumbers:{self.winningNumbers}'

    @staticmethod
    def create(lineData):
        cardData = lineData.split(':')
        id = cardData[0].strip().split(' ')[1]

        n = cardData[1].strip().split('|')

        winningNumbers = n[0].strip().split(' ')
        # filter out empty strings
        winningNumbers = [v for v in winningNumbers if v]
        numbers = n[1].split(' ')
        numbers = [v for v in numbers if v]

        return Card(id, winningNumbers, numbers)




def parseFile(filepath):
    cards = Cards()

    file = open(filepath, 'r')

    for line in file:
        cards.append(Card.create(line))
    file.close()

    return cards


def calculatePoints(filename):
    cards = parseFile(filename)
    result = 0
    for card in cards.cards:
        winningNumbers =card.winningNumbers
        numbers = card.numbers
        numberOfMatches = len(list(set(winningNumbers).intersection(numbers)))
        points = int(2**(numberOfMatches - 1))
        result += points

    return result

