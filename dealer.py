class Dealer:
    def __init__(self):
        self.hand = None # The reason that is None is because the game hasn't started yet
    
    def get_str_hand(self):
        return str(self.hand) # This is the string representation of the hand

    def hit(self, card):
        self.hand.add(card)
        
#This class we are going to use to represent the dealer
#we have 3 methods init, get_str_hand, and hit 
#init is the constructor, it is going to initialize the dealer's hand to None
#get_str_hand is going to return the string representation of the hand
#hit is going to add a card to the dealer's hand