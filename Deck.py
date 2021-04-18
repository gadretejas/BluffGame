import random
from Card import Card

class Deck(object):
	"""docstring for Deck"""
	def __init__(self, shuffled = False):
		'''initialises the deck of cards.'''
		self.cardList = []

		# make all cards and put in the list
		suites = ['hearts', 'diamonds', 'spades', 'clubs']
		for suite in suites:
			for value in range(1, 14):
				#make new card
				self.cardList.append(Card(suite, value))

		# make jokers and add them to the deck
		j1 = Card(special, -1)
		j2 = Card(special, -1)

		self.cardList.append(j1)
		self.cardList.append(j2)

		if shuffled:
			random.shuffle(self.cardList)


	def __str__(self):
		'''returns the string representation of the deck.'''
		return str([str(card) for card in self.cardList])

	def shuffle(self):
		'''Shuffles the deck.'''
		random.shuffle(self.cardList)

	def topCard(self):
		'''returns the top card in the deck and takes ot out of the deck.'''
		# take card out of the list
		retCard = self.cardList[0]
		# remove card from deck
		self.cardList = self.cardList[1:]
		# return the card
		return retCard

	def bottomCard(self):
		'''returns the bottom card in the deck and takes ot out of the deck.'''
		# take card from deck
		retCard = self.cardList[-1]
		# remove card from deck
		self.cardList = self.cardList[:-1]
		# return the card
		return retCard

	def cutAtPosition(self, position):
		'''Cuts the deck at given position. 
		lower part od deck comes on top of the upper part of the deck.'''
		assert position in range(1, len(self.cardList)+1), 'illegal value passed. position should be between 1 and 52'
		# cut the list at the position
		l1, l2 = self.cardList[:position], self.cardList[position:]
		# merge them in reverse order
		self.cardList = l2 + l1

	def getCardAtPosition(self, position):
		assert position in range(1, len(self.cardList)+1), 'illegal value passed. position should be between 1 and 52'
		# take the card from deck
		retCard = self.cardList[position-1]
		# remove card from deck
		self.cardList.pop(position-1)
		# return the card
		return retCard

	def addCardOnTop(self, newCard):
		assert type(newCard) == Card, 'insert a card.'
		# insert on top
		self.cardList = [newCard] + self.cardList

	def addCardAtPosition(self, position, newCard):
		assert position in range(1, len(self.cardList)+1), 'illegal value passed. position should be between 1 and 52'
		# break up the deck in that position
		position = position-1
		l1, l2 = self.cardList[:position], self.cardList[position:]
		# add card at position
		self.cardList = l1 + [newCard] + l2

	def reset(self):
		# deck goes to the original state, shuffled or ubshuffled
		suites = ['hearts', 'diamonds', 'spades', 'clubs']
		for suite in suites:
			for value in range(1, 14):
				#make new card
				self.cardList.append(Card(suite, value))

		if shuffled:
			random.shuffle(self.cardList)



if __name__ == "__main__":
	newDeck = Deck()
	print(newDeck)
	print()
	
	print(newDeck.bottomCard())
	print(newDeck)
	print()

	newDeck.cutAtPosition(10)
	print(newDeck)

	newCard = newDeck.getCardAtPosition(10)
	print(newDeck)
	print()
	newDeck.addCardAtPosition(2, newCard)
	print(newDeck)















