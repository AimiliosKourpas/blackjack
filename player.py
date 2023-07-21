from dealer import Dealer


class Player(Dealer): # DEALER IS THE PARENT CLASS OF PLAYER INHERITANCE
    def __init__(self , balane):
        super().__init__() # This is going to call the constructor of the parent class
        self.balance = balane # This is going to initialize the balance of the player