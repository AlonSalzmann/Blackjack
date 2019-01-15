from objects import Deck

print('Welcome to Blackjack!')

deck = Deck.Deck()
deck.shuffle()

dealer_cards = []
player_cards = []

dealer_cards.append(deck.draw())
player_cards.append(deck.draw())
dealer_cards.append(deck.draw())
player_cards.append(deck.draw())

print "player's cards --> " + str(player_cards) + " \ndealer's cards --> " + str(dealer_cards)

player_card_numbers = []
for card in player_cards:
    player_card_numbers.append(card.number)

dealer_card_numbers = []
for card in dealer_cards:
    dealer_card_numbers.append(card.number)


def player_turn():
    if sum(player_card_numbers) < 21:
        user_decision = input('would you like to hit or hold?')
        if user_decision == 'hit':
            player_cards.append(deck.draw())
            print player_cards, dealer_cards
            player_turn()

        elif user_decision == 'hold':
            print "Dealer's turn!"
            dealer_turn()
        else:
            print "player must choose 'hit' or 'hold'"
            player_turn()

    elif sum(player_card_numbers) == 21:
        print "Blackjack!"
        dealer_turn()

    else:
        print "Player Burnt! \nDealer's turn!"
        dealer_turn()


def dealer_turn():
    if sum(dealer_card_numbers) < 17:
        dealer_cards.append(deck.draw())

    elif 17 <= sum(dealer_card_numbers) <= 21:
        print "Dealer holds"
        print dealer_cards
        score()

    elif sum(dealer_card_numbers) == 21:
        print "It's a draw!"
        score()

    else:
        print "Dealer burnt!"
        score()


def score():
    if sum(player_card_numbers) > sum(dealer_card_numbers):
        print "Player wins round!"
        return 1

    elif sum(player_card_numbers) < sum(dealer_card_numbers):
        print "Dealer wins round!"
        return -1

    else:
        print "It's a tie!"
        return 0


player_turn()

'''Traceback (most recent call last):
  File "C:/Users/pc/PycharmProjects/Blackjack/Game Flow/Game_Flow.py", line 83, in <module>
    player_turn()
  File "C:/Users/pc/PycharmProjects/Blackjack/Game Flow/Game_Flow.py", line 29, in player_turn
    user_decision = input('would you like to hit or hold?')
  File "<string>", line 1, in <module>
NameError: name 'hit' is not defined'''