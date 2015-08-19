from deck import *
from idiots_delight import *

def main():
	num_games = 1
	results = [0]*num_games
	for i in range(num_games):
		deck = Deck()
		deck.shuffle_deck()
		game = Idiots_Delight(deck=deck)
		cards_remaining = game.play_game()
		results[i] = cards_remaining
	print results

main()