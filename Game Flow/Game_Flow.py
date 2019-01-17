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

player_money = 500
player_bet = min(500, input('you have ' + str(player_money) + ' dollars, please place bet: '))

print "player's cards --> " + str(player_cards) + " \ndealer's cards --> " + str(dealer_cards)

player_card_numbers = []
for card in player_cards:
    player_card_numbers.append(card.number)

dealer_card_numbers = []
for card in dealer_cards:
    dealer_card_numbers.append(card.number)


def player_turn():
    if sum(player_card_numbers) < 21:
        user_decision = raw_input('would you like to hit or hold?')
        if user_decision == 'hit':
            player_cards.append(deck.draw())
            player_card_numbers.append(card.number)
            if sum(player_card_numbers) == 21:
                print "player's cards --> " + str(player_cards) + " \ndealer's cards --> " + str(dealer_cards)
                print "Blackjack!"
                dealer_turn()
            elif sum(player_card_numbers) < 21:
                print "player's cards --> " + str(player_cards) + " \ndealer's cards --> " + str(dealer_cards)
                player_turn()
            else:
                print "player's cards --> " + str(player_cards) + " \ndealer's cards --> " + str(dealer_cards)
                print "Player Burnt! \nDealer's turn!"
                dealer_turn()

        elif user_decision == 'hold':
            print "Dealer's turn!"
            dealer_turn()
        else:
            print "player must choose 'hit' or 'hold'"
            player_turn()

    elif sum(player_card_numbers) == 21:
        print "player's cards --> " + str(player_cards) + " \ndealer's cards --> " + str(dealer_cards)
        print "Blackjack!"
        dealer_turn()

    else:
        print "player's cards --> " + str(player_cards) + " \ndealer's cards --> " + str(dealer_cards)
        print "Player Burnt! \nDealer's turn!"
        dealer_turn()


def dealer_turn():
    if sum(dealer_card_numbers) < 17:
        dealer_cards.append(deck.draw())
        dealer_card_numbers.append(card.number)
        dealer_turn()

    elif 17 <= sum(dealer_card_numbers) < 21:
        print "player's cards --> " + str(player_cards) + " \ndealer's cards --> " + str(dealer_cards)
        print "Dealer holds"
        score()

    elif sum(dealer_card_numbers) == 21 and sum(player_card_numbers) == 21:
        print "player's cards --> " + str(player_cards) + " \ndealer's cards --> " + str(dealer_cards)
        print "It's a draw!"
        score()

    elif sum(dealer_card_numbers) == 21:
        print "player's cards --> " + str(player_cards) + " \ndealer's cards --> " + str(dealer_cards)
        print "Blackjack to dealer!"
        score()

    elif sum(dealer_card_numbers) > 21:
        print "player's cards --> " + str(player_cards) + " \ndealer's cards --> " + str(dealer_cards)
        print "Dealer burnt!"
        score()


def score():
    if 21 >= sum(player_card_numbers) > sum(dealer_card_numbers):
        print "Player wins round!"
        updated_money = player_money + player_bet
        print "you have won " + str(player_bet) + " dollars!"
        print "you now have " + str(updated_money) + " dollars!"
        next_round()

    elif sum(player_card_numbers) <= 21 < sum(dealer_card_numbers):
        print "Dealer burnt! \nPlayer wins round!"
        updated_money = player_money + player_bet
        print "you have won " + str(player_bet) + " dollars!"
        print "you now have " + str(updated_money) + " dollars!"
        next_round()

    elif 17 <= sum(dealer_card_numbers) <= 21 and sum(dealer_card_numbers) > sum(player_card_numbers):
        print "Dealer wins round!"
        updated_money = player_money - player_bet
        print "you have lost " + str(player_bet) + " dollars!"
        print "you now have " + str(updated_money) + " dollars!"
        next_round()

    elif 17 <= sum(dealer_card_numbers) <= 21 < sum(player_card_numbers):
        print "Player burnt! \nDealer wins round!"
        updated_money = player_money - player_bet
        print "you have lost " + str(player_bet) + " dollars!"
        print "you now have " + str(updated_money) + " dollars!"
        next_round()

    else:
        print "It's a tie!\nmoney returns to hand"
        next_round()


def next_round():
    next_rnd = raw_input('would you like to play another round? ')
    while next_rnd == 'yes':
        del player_cards[:]
        del dealer_cards[:]
        del player_card_numbers[:]
        del dealer_card_numbers[:]
        deck.shuffle()
        dealer_cards.append(deck.draw())
        player_cards.append(deck.draw())
        dealer_cards.append(deck.draw())
        player_cards.append(deck.draw())
        print "player's cards --> " + str(player_cards) + " \ndealer's cards --> " + str(dealer_cards)
        player_turn()
    if next_rnd == 'no':
        print "goodbye"
        quit()
    else:
        print "player must choose between 'yes' and 'no'..."
        next_round()


player_turn()
