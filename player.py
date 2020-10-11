from deck import Deck

class Player(object):
    """Class representing the player."""
    
    def __init__(self, name):
        """Initialise attributes for the Player class."""
        self.name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.draw_card())
        return self

    def show_hand(self):
        for card in self.hand:
            card.show()

    def discard(self):
        return self.hand.pop()
        # We could also take in a suit and a value (in the parameters), if we 
        # had a particular card in our hand and discard it. Would have to code
        # in that logic.





























