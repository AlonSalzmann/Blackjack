class Card(object):
    "Card object containing a number and a symbol"
    def __init__(self, number, symbol):
        self.number = number
        self.symbol = symbol

    def __str__(self):
        return "symbol: {}, number: {}".format(self.symbol, self.number)

    def __repr__(self):
        return str(self)


card_numbers = range(1, 14, 1)
card_symbols = ["spades", "hearts", "diamonds", "clubs"]
