import random
from .Card import Card, card_numbers, card_symbols


class Deck(object):
    def __init__(self):
        self.cards = []
        for number in card_numbers:
            for symbol in card_symbols:
                temp_card = Card(number, symbol)
                self.cards.append(temp_card)

    def draw(self):
        return self.cards.pop(0)

    def shuffle(self):
        temp_cards = {}
        for card in self.cards:
            random_number = random.random()
            temp_cards[random_number] = card
        temp_numbers = temp_cards.keys()  # .keys() return a list of the dict keys
        temp_numbers.sort()
        temp_order = []
        for number in temp_numbers:
            temp_order.append(temp_cards[number])
        self.cards = temp_order
        return self.cards

