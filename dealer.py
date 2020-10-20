from deck import Deck  # May not need
from card import Card

class Dealer:
    """Class representing the dealer."""
    
    def __init__(self, dealer):
        """Initialise attributes for the Dealer class."""
        self.card = Card()

        self.name = dealer
        self.hand = self.card.dealer_cards

    def draw(self, deck):
        self.hand.append(deck.draw_card())
        return self

    def show_hand(self):
        for card in self.hand:
            self.card.blitme()  # Could possible replace this with the blitme() 
                         # function.

    def discard(self):
        return self.hand.pop()
        # We could also take in a suit and a value (in the parameters), if we 
        # had a particular card in our hand and discard it. Would have to code
        # in that logic.

































