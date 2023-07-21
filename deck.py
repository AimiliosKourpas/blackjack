import random
from card import Card


class Deck:
    def __init__(self):
        self.cards = []
        self.create_deck()
        self.shuffle()

    def create_deck(self):
        for suit in range(4):
            for card in range(1, 14):
                new_card = Card(suit, card)
                self.cards.append(new_card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num_cards):
        dealt_cards = []

        for idx in range(num_cards):
            # we will treat the end of the list as the top of the deck
            top_card = self.cards.pop()
            dealt_cards.append(top_card)

        return dealt_cards
    
#So here we have a class thats going to represent the deck
# in init we create an empty list of cards 
#the methos are create_deck, shuffle, and deal
#create_deck is going to create a deck of cards
#shuffle is going to shuffle the deck of cards
#deal is going to deal a certain number of cards