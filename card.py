import pygame as pg
import random

class Card(object):
    """Class resembling a card."""

    def __init__(self, value, suit):
        """Initialise the attribute for the card class."""
        self.suits = {'S':'spades', 'H':'hearts', 'D':'diamonds', 'C': 'clubs'}
        self.values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, 
                        '9':9,'T':10, 'J':10, 'Q':10, 'K':10, 'A':[1, 11] }
        
        card_images = {}
        for suit in self.suits:
            for symbol in self.values.keys():
                card_name = f"{suit}_{symbol}"
                folder_name = pg.image.load(f'cards/{card_name}.png')
                card_images[card_name] = folder_name

        # Player cards
        self.player_cards = []
        self.player_score = 0

        # Dealer cards
        self.dealer_cards = []
        self.dealer_score = 0

    # Get to work properly
    def blitme(self):
        """Draws the cards onto the screen."""
        self.screen.blit(self.deck.playing_deck)





































