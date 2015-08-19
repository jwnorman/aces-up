import sys
import itertools
import numpy as np

class Deck(object):

	def __init__(self, suit_labels = ['D', 'H', 'C', 'S'],
		card_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]):

		self.suit_labels = suit_labels
		self.card_values = card_values
		self.card_pool = list(itertools.product(self.suit_labels,\
			self.card_values))
		self.num_tot_cards = len(self.card_pool)
		self.num_suits = len(self.suit_labels)
		self.num_cards = len(self.card_values)

	def shuffle_deck(self):
		np.random.shuffle(self.card_pool)