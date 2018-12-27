from objects import Deck

print('Welcome to Blackjack!')

deck = Deck.Deck()

dealer_cards = []
player_cards = []

dealer_cards.append(deck.draw())
player_cards.append(deck.draw())
dealer_cards.append(deck.draw())
player_cards.append(deck.draw())

print(dealer_cards, player_cards)


def player_turn():
    player_card_numbers = []
    for card in player_cards:
        player_card_numbers.append(card.number)

    while sum(player_card_numbers) < 21:
        user_decision = input('would you like to hit or hold?')
        if user_decision == 'hit':
                player_cards.append(deck.draw())
                print(player_cards, dealer_cards)
                player_turn()

        elif user_decision == 'hold':
            print("Dealer's turn")
            dealer_turn()
        else:
            print("player must choose 'hit' or 'hold'")
            player_turn()

    if sum(player_card_numbers) == 21:
        print("Blackjack!")
        dealer_turn()

    else:
        print("Player Burnt!")
        dealer_turn()


def dealer_turn():
    dealer_card_numbers = []
    for card in dealer_cards:
        dealer_card_numbers.append(card.number)

    while sum(dealer_card_numbers) < 17:
        dealer_cards.append(deck.draw())
    if 17 <= sum(dealer_cards) <= 21:
        print("Dealer holds")
    else:
        print("Dealer burnt")


player_turn()

