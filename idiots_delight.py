from deck import *
from collections import defaultdict
import operator

class Idiots_Delight(object):

	def __init__(self, num_piles=4, deck=None):
		self.num_piles = num_piles
		self.piles = defaultdict(list)
		self.deck = deck
		if self.deck.__class__.__name__ != 'Deck':
			print 'The deck should be of type "Deck"'
		if len(self.deck.card_pool) % self.num_piles != 0:
			'The number of cards should be a multiple of the number of cards.'
		if self.num_piles != self.deck.num_suits:
			'The number of piles should be equal to the number of suits.'

	def play_game(self):
		while len(self.deck.card_pool) > 0:
			self.add_layer()
			print 'New layer:'
			print self.piles
			print ''
			self.eliminate()

		num_cards_remaining = 0
		for pile, cards in self.piles.iteritems():
			num_cards_remaining += len(cards)

		return num_cards_remaining

	def add_layer(self):
		for pile_num in range(self.num_piles):
			self.piles[pile_num].append(self.deck.card_pool.pop())

	def eliminate(self):
		something_changed = False
		
		cards_showing = self.get_cards_showing()

		# Find high card for each suit
		high_card_per_suit = dict(zip(self.deck.suit_labels, [None]*self.num_piles))
		for pile, card in cards_showing.iteritems():
			if len(card) > 0:
				if card[1] > high_card_per_suit[card[0]]:
					high_card_per_suit[card[0]] = card[1]

		# Remove cards
		for pile, card in cards_showing.iteritems():
			if len(card) > 0:
				if card[1] < high_card_per_suit[card[0]]:
					something_changed = True
					self.piles[pile].pop()

		if something_changed:
			print 'Cards removed:'
			print self.piles
			print ''
			self.eliminate()
		else:
			reorg = self.is_reorganizable()
			if reorg:
				self.reorganize()
				self.eliminate()

	def get_cards_showing(self):
		cards_showing = dict()
		for pile_num in range(self.num_piles):
			pile_size = len(self.piles[pile_num])
			if pile_size == 0:
				cards_showing[pile_num] = []
			if pile_size > 0:
				cards_showing[pile_num] = self.piles[pile_num][pile_size-1]

		return cards_showing

	def is_reorganizable(self):
		has_zero = False
		has_many = False
		for pile, cards in self.piles.iteritems():
			if len(cards) == 0:
				has_zero = True
			if len(cards) > 1:
				has_many = True
		if has_zero and has_many:
			return True
		else:
			return False

	def reorganize(self):
		# move pile that has more than one care with largest sum
		# to pile with zero
		pile_sums = defaultdict(int)
		for pile, cards in self.piles.iteritems():
			if len(cards) > 1:
				for card_num in range(len(cards)):
					pile_sums[pile] += cards[card_num][1]
					if card_num == len(cards)-1 and \
					cards[card_num][1] == max(self.deck.card_values):
						pile_sums[pile] += float('inf')
			if len(cards) == 0:
				pile_to_receive = pile
		
		pile_to_move = max(pile_sums.iteritems(), key=operator.itemgetter(1))[0]
		card_to_move = self.piles[pile_to_move].pop()
		self.piles[pile_to_receive].append(card_to_move)

		print 'Reorganized:'
		print self.piles
		print ''




