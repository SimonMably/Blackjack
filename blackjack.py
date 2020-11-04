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

class Deck:
    """Class represents a deck of cards."""
    def __init__(self):
        self.cards = []
        self.build_deck()

    def build_deck(self):
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

class Player:
    """Class represents the player."""
    def __init__(self, name):
        self.name = name
        self.hand = []

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









