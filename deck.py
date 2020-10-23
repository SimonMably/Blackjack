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

    def build_deck(self):
        """Build deck of cards."""
        for suit in self.suits[self.card.suit]:
            for value in self.values[self.card.value]:
                self.cards.append(Card(self.suit, self.value))
                print(self.cards)