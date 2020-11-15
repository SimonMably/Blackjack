import random

# Classes

class Card:
    """Class representing a card."""
    
    def __init__(self, suit, value):
        """Initialise Card class attributes."""
        self.suit = suit
        self.value = value

    def show(self):
        """Prints a properly formatted playing card."""
        print(f"{self.value} of {self.suit}")

# -----------------------------------------------------------------------------

class Deck:
    """Class representing a deck of cards."""

    def __init__(self):

        """Initialise Deck class attributes."""
        self.cards = []
        self.build_deck()

    def build_deck(self):
        """Builds deck of cards."""

        for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
            for value in range(1, 14):
                if value == 1:
                    value = "Ace"
                if value == 11:
                    value = "Jack"
                if value == 12:
                    value = "Queen"
                if value == 13:
                    value = "King"
                self.cards.append(Card(suit, value))
        # IDEA: Include if-else statements to turn the numbers (from range())
        #       1, 11, 12, and 13 into 'Ace', 'Jack', 'Queen', and 'King'
    
    def show(self):
        for card in self.cards:
            card.show()
    
    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
    
    def draw_card(self):
        # Removes card from the top of the deck (or end of the deck list).
        # Return will return the removed card to whichever method called 
            # draw_card()
        return self.cards.pop()

# -----------------------------------------------------------------------------

class Player:
    """Class representing the player."""

    def __init__(self, name="Player"):
        self.name = name
        self.hand = []

    def draw(self, deck):
        """Draws cards for the player."""
        self.hand.append(deck.draw_card())
        return self  # return self will allow the 'draw' method to be chained

    def show_hand(self):
        """Shows cards in players hand."""
        for card in self.hand:
            card.show()
    
    def discard(self):
        """Discards a card from players hand."""
        # Could add logic this method, eg. take in sui and value as arguments
        # and look through player hand and discard certain card from player 
        # hand, if there.
        return self.hand.pop()
    
    def hit(self):
        """Add new card to player hand."""
        pass

    def stay(self):
        """End player turn."""
        pass

    def winner(self):
        """Announce player win, end game and offer new game."""
        pass

# -----------------------------------------------------------------------------

class Dealer:
    """Class representing the dealer."""

    def __init__(self, name="Dealer"):
        self.name = name
        self.hand = []

    def draw(self, deck):
        """Draws cards for the dealer."""
        self.hand.append(deck.draw_card())
        return self  # return self will allow the 'draw' method to be chained

    def show_hand(self):
        """Shows cards in dealers hand."""
        for card in self.hand:
            card.show()
    
    def discard(self):
        """Discards a card from dealers hand."""
        return self.hand.pop()

    def hit(self):
        """Add new card to dealer hand."""
        pass

    def stay(self):
        """End dealer turn."""
        pass

    def winner(self):
        """Announce dealer win, end game and offer player new game."""
        pass

# -----------------------------------------------------------------------------

class Game:
    """Class managing the whole game."""

    def __init__(self):
        """Initialise the Game class attributes."""
        self.deck = Deck()
        self.card = Card()
        self.player = Player()
        self.dealer = Dealer()

        # True bool value for main game loop.
        self.active_game = True

    def run_game(self):
        """Start the main loop for the game."""
        while self.active_game:
            pass

    def start_new_game(self):
        """Start a new game. 
        If a game has been played, offer player the choice to play again."""
        pass

    def calculate_hand(self):
        """Keep track of value of all cards in player/dealer hand."""
        # Add values for all cards in Player hand.
        # Add values for all cards in Dealer hand.

        # IDEA: add the self.card.value for all card in player/dealer hand
        #       to get overall hand value.
        pass

    def compare_hand_values(self):
        """Compares the overall values for players and dealers hands."""
        # IF value of Player hand == 21 and value of Dealer hand <= 20
            # or value of Player hand > value of Dealer hand, Player wins.
        # IF value of Dealer hand == 21 and value of Player hand <= 20
            # or value of Dealer hand > value of Player hand, Dealer wins.

        # IDEA: add the self.card.value for all card in player/dealer hand
        #       to get overall hand value.
        pass



# -----------------------------------------------------------------------------

# This will make sure that the game runs. FULLY OOP OPERATIONAL ONLY.
'''
if __name__ == '__main__':
    game = Game()
    game.run_game()
'''
# -----------------------------------------------------------------------------

"""
card = Card("Clubs", 6)
card.show()

deck = Deck()
deck.shuffle()
deck.show()

print("\n")

card = deck.draw_card()
card.show()

print("\n")
"""
deck = Deck()
deck.shuffle()

print("")

player = Player()
print(player.name)            # Prints the default name 'Player'
player.draw(deck).draw(deck)  # Draws 2 random cards
player.show_hand()            # Shows cards in Player hand.

print("")

dealer = Dealer()
print(dealer.name)            # Prints the default name 'Dealer'
dealer.draw(deck).draw(deck)  # Draws 2 random cards
dealer.show_hand()            # Shows cards in Dealer hand.
