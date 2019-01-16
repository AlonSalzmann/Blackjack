class Card(object):
    def __init__(self, number, symbol):
        self.number = number
        self.symbol = symbol

    def __str__(self):
        return "symbol: {}, number: {}".format(self.symbol, self.number)

    def __repr__(self):
        return str(self)


card_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]
card_symbols = ["spades", "hearts", "diamonds", "clubs"]
