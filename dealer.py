from deck import Deck
from card import Card

class Dealer:
    """Class representing the dealer."""
    
    def __init__(self, dealer):
        """Initialise attributes for the Dealer class."""
        self.card = Card()

        self.name = dealer
        # self.hand = self.card.dealer_cards

    def deal_cards(self):
        """
        Deals cards to Player and Dealer from the top of the deck of cards.
        """
        # Take 2 cards from deck of cards and place into player_hand list and 
        # again for dealer_hand list
        pass

    def draw(self, deck):
        """Dealer draws a card or cards from the deck."""
        pass

    def show_hand(self):
        """Show dealers hand on-screen."""
        # Implement blitme() function here.
        pass

    def discard(self):
        """Dealer can discard a card or cards from dealers hand."""
        # May not use
        pass