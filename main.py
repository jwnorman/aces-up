from deck import Deck
from idiots_delight import Idiots_Delight


def main():
    # num_games = 1
    # results = [0]*num_games
    # for i in range(num_games):
    #     deck = Deck()
    #     deck.shuffle_deck()
    #     game = Idiots_Delight(deck=deck, print_steps=True)
    #     cards_remaining = game.play_game()
    #     results[i] = cards_remaining
    # print results

    num_games = 100
    results = [0] * num_games
    for i in range(num_games):
        deck = Deck(suit_labels=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
                    card_values=[1, 2, 3, 4])
        deck.shuffle_deck()
        game = Idiots_Delight(deck=deck)
        cards_remaining = game.play_game()
        results[i] = cards_remaining
    print results

main()
