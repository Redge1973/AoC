import re


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

    def copy(self):
        return Card(self.id, self.winningNumbers, self.numbers)

    def numberOfMatches(self):
        return len(list(set(self.winningNumbers).intersection(self.numbers)))

    @staticmethod
    def create(lineData):
        cardData = lineData.split(':')
        pattern = r"Card\s+(\d+)"
        match = re.search(pattern, cardData[0])
        id = match.group(1)
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
        numberOfMatches = card.numberOfMatches()
        points = int(2**(numberOfMatches - 1))
        result += points

    return result

def calculateNumberOfCards(filename):
    cards = parseFile(filename)

    cardList = cards.cards

    sortedCards = {}
    for card in cardList:
        sortedCards[card.id] = [card]

    for j in range(1, len(sortedCards)+1):
        cards = sortedCards[f'{j}']
        for card in cards:
            matches = card.numberOfMatches()

            for i in range(1, matches+1):
                index = f'{j+i}'
                sortedCards[index].append(sortedCards[index][0].copy())

    return len(sum(sortedCards.values(), []))

