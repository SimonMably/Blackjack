import pygame as pg
import random

from card import Card

class Deck(object):
    """Class regarding the deck of cards."""

    def __init__(self):
        """Initialise attributes for the Deck class."""
        self.card = Card()

        self.cards = []
        self.build_deck()

    def build_deck(self):  # SEE IF WORKS
        for suit in self.suits[self.card.suits]:
            for values in self.values[self.card.values]:
                pass  # FIGURE OUT HOW TO DO THIS.
                      # THEN, SEE IF THIS FUNCTION WORKS.
                # self.cards.append(Card(suit, value))
                # print "{} of {}".format(value, suit) 
                # ^^^ As shown in YouTube tutorial "Python OOP - Deck of Cards"
                    # By YT user: Executed Binary

    def show(self):
        """
        Placeholder Function:
        
        Will be replaced by either the 'blitme' function or other function that 
        will show that a deck of cards has been made.
        """
        for c in self.cards:
            c.show()
    
    def shuffle_deck(self):
        random.shuffle(self.playing_deck)
    
    def draw(self):
        return self.cards.pop()



























