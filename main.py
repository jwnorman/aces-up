from deck import Deck
from idiots_delight import Idiots_Delight


def main():
    # num_games = 1
    # results = []
    # for i in range(num_games):
    #     deck = Deck()
    #     deck.shuffle_deck()
    #     game = Idiots_Delight(deck=deck, print_steps=True)
    #     cards_remaining = game.play_game()
    #     results.append(cards_remaining)
    # print results

    num_games = 10000
    results = []
    for i in range(num_games):
        deck = Deck()
        deck.shuffle_deck()
        game = Idiots_Delight(deck=deck)
        cards_remaining = game.play_game()
        results.append(cards_remaining)
    print results

main()
