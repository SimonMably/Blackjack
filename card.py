import pygame as pg
import random

class Card:
    """Class representing a card or cards."""

    def __init__(self, value, suit):
        """Initialise the attribute for the card class."""
        self.suits = {'S':'spades', 'H':'hearts', 'D':'diamonds', 'C': 'clubs'}
        self.values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, 
                        '9':9,'10':10, 'jack':10, 'queen':10, 'king':10, 
                        'ace':[1, 11] }
        
        """
        card_images = {}
        for suit in self.suits.values():
            for value in self.values.keys():
                card_name = f'{value}_{suit}'
                folder_name = pg.image.load(f'cards/{card_name}.png')
                card_images[card_name] = folder_name
        """

        # Player cards
        self.player_cards = []
        self.player_score = 0

        # Dealer cards
        self.dealer_cards = []
        self.dealer_score = 0

    def get_card_image(self):
        card_images = {}
        for suit in self.suits.values():
            for value in self.values.keys():
                card_name = f'{value}_{suit}'
                folder_name = pg.image.load(f'cards/{card_name}.png')
                card_images[card_name] = folder_name

    def show(self):
        """Placeholder Function
        iNCORPORATE INOT BLITME() IF POSSIBLE.
        """
        print(f'{self.values} of {self.suits}')

    # Get to work properly
    def blitme(self):
        """Draws the cards onto the screen."""
        self.screen.blit(self.deck.playing_deck)





































