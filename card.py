import pygame as pg
import random

class Card():
    """Class resembling a card."""

    def __init__(self, value, suit):
        """Initialise the attribute for the card class."""
        self.suits = {'S':'spades', 'H':'hearts', 'D':'diamonds', 'C': 'clubs'}
        self.values = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, 
                        '9':9,'T':10, 'J':11, 'Q':12, 'K':13}
        
        card_images = {}
        for suit in self.suits:
            for symbol in self.values.keys():
                card_name = f"{suit}{symbol}"
                folder_name = pg.image.load(f'cards/{card_name}.png')
                card_images[card_name] = folder_name



        self.player_hand = []
        self.player_score = 0
        self.dealer_hand = []
        self.dealer_score = 0







































