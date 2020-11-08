# Imports
import random

# -----------------------------------------------------------------------------
# Classes

class Card:
    """Class represents a playing card."""
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print(f"{self.value} of {self.suit}")

# -----------------------------------------------------------------------------

class Deck:
    """Class represents a deck of cards."""
    def __init__(self):
        self.cards = [Card(s, v) for s in ["Spades", "Clubs", "Hearts",
                      "Diamonds"] for v in ["A", "2", "3", "4", "5", "6", 
                      "7", "8", "9", "10", "J", "Q", "K"]]
        #self.build_deck()

    def build_deck(self):  # MAY NOT USE 
        """MAY NOT USE"""
        # s == suit
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            # v == value
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    def show(self):
        for card in self.cards:
            card.show()

    def shuffle(self):
        # Uses the Fisher Yates Shuffle algorithm to shuffle the deck of cards.
        for i in range(len(self.cards) -1, 0, -1):
            # r == random number
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw_card(self):
        return self.cards.pop()

# -----------------------------------------------------------------------------

class Player:
    """Class represents the player."""
    def __init__(self, name):
        self.game = Game()
        self.name = self.get_name(name)
        self.hand = []

    def get_name(self):
        self.game.get_name()

    def draw(self, deck):
        self.hand.append(deck.draw_card())
        return self  # Will be able to draw multiple cards.

    def show_hand(self):
        for card in self.hand:
            card.show()

    def discard(self):
        return self.hand.pop()
        # Could add logic to this. For example, this method could take a suit
        # and a value, the logic can find out if a card in player hand matches
        # the suit/value and discard the card if it is in the players hand.

# -----------------------------------------------------------------------------

class Dealer:
    """Class represents the dealer."""
    def __init__(self, name='dealer'):
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.draw_card())
        return self

    def show_hand(self):
        for card in self.hand:
            card.show()

# -----------------------------------------------------------------------------

class Game:
    """Main class for the game."""
    def __init__(self):
        """Initialise attributes."""
        self.dealer = Dealer()
        self.player = Player()
        self.deck = Deck()
        self.card = Card()

    def play_game(self):
        """Main game loop."""
        while True:
            self.get_name()

    def get_name(self, name):
        self.ask_name = str(input("Enter your name: "))
        self.ask_name = self.player(name)
        

# -----------------------------------------------------------------------------
"""
# Class Instances

#card = Card("Clubs", 6)
# card.show()

deck = Deck()
deck.shuffle()
#deck.show()

print("Player: Simon")
simon = Player("Simon")
simon.draw(deck).draw(deck)  # Draws 2 cards.
simon.show_hand()

# discard() will remove the last card in players hand
simon.discard()
simon.show_hand()

print("\nDealer")
dealer = Dealer()
dealer.draw(deck).draw(deck)
dealer.show_hand()
"""
# -----------------------------------------------------------------------------




# """

if __name__ == '__main__':
    blackjack = Game()
    blackjack.play_game()



