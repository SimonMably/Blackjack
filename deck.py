import pygame as pg
import random

from card import Card

class Deck:
    """Class representing a deck of cards."""

    def __init__(self):
        """Initialise attributes for the Deck class."""
        self.card = Card()

        self.cards = []
        self.build_deck()

    def build_deck(self):  # SEE IF WORKS
        """Builds deck of cards"""
        for suit in self.suits[self.card.suit]:
            for value in self.values[self.card.value]:
                #pass  # FIGURE OUT HOW TO DO THIS.
                      # THEN, SEE IF THIS FUNCTION WORKS.
                self.cards.append(Card(suit, value))
                # print(f"{self.value} of {self.suits}") ## May not need.
                # ^^^ Convert this into something that Pygame can use

    def show(self):
        """
        Placeholder Function:

        Will be replaced by either the 'blitme' function or other function that 
        will show that a deck of cards has been made. 

        MAY BE ABLE TO COMBINE THIS FUNCTION INTO BLITME() method.
        """
        for c in self.cards:
            c.show()  # May be possible to call blitme() function from Card()
                      # here. Could replace show() method with blitme() method.
    
    def shuffle_deck(self):
        """Uses the Fisher–Yates shuffle algorithm to shuffle deck of cards."""
        # For loop starts at the end of 'self.cards' list (1st index: -1, goes
        #  to beginning of list (index: 0), for loop decrements from end to 
        # beginning of list with the second -1)
        for i in range(len(self.cards)-1, 0, -1):  # This will show 51 - 1
            # pick random number to the left of our current poition.
            r = random.randint(0, i)
            # Swaps 2 cards. 
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
        ### MAKE SURE THIS FUNCTION WORKS!!!!
    
    def draw_card(self):
        # Picks out card from end of cards list (or top of the deck)
        return self.cards.pop()



























