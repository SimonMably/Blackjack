import random

class Card:
    """Class representing a card."""
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        print(f"{self.value} of {self.suit}")

# -----------------------------------------------------------------------------

class Deck:
    """Class representing a deck of cards."""
    def __init__(self):
        self.cards = []
        self.build_deck()

    def build_deck(self):
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
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.draw_card())
        return self  # return self will allow the 'draw' method to be chained

    def show_hand(self):
        for card in self.hand:
            card.show()
    
    def discard(self):
        # Could add logic this method, eg. take in sui and value as arguments
        # and look through player hand and discard certain card from player 
        # hand, if there.
        return self.hand.pop()

# -----------------------------------------------------------------------------

class Dealer:
    """Class representing the dealer."""
    def __init__(self):
        pass

# -----------------------------------------------------------------------------

class Game:
    """Class managing the whole game."""
    def __init__(self):
        pass

# -----------------------------------------------------------------------------

#card = Card("Clubs", 6)
#card.show()

deck = Deck()
#
deck.shuffle()
#deck.show()


#card = deck.draw_card()
#card.show()

bob = Player("Bob")
bob.draw(deck).draw(deck)
bob.show_hand()

