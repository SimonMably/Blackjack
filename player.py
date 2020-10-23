class Player:
    """Class representing the player."""
    
    def __init__(self, name):
        """Initialise attributes for the Player class."""
        self.name = name
        
        # Attribute for Players hand
        # eg.
        # self.hand = self.card.players_cards  # this would be a list/empty list
                                               # in Card class, perhaps.
        
    def draw(self):
        pass

    def show_hand(self):
        pass
        # Find a way to implement blitme() function.
    
    def discard(self):
        # Discard a card from hand.
        pass
