import pygame as pg
import random


class Card:
    """Class representing a card or cards."""
    #  values, suits, <--- include in __init__ method parameters
    def __init__(self, image, b_game):
        """Initialise the attribute for the card class."""
        self.suits = {'S':'spades', 'H':'hearts', 'D':'diamonds', 'C': 'clubs'}
        self.values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, 
                        '9':9,'10':10, 'jack':10, 'queen':10, 'king':10, 
                        'ace':[1, 11] }
        
        self.screen = b_game.screen
        self.settings = b_game.settings
        self.screen_rect = b_game.screen.get_rect()

        # Player cards
        self.player_cards = []
        self.player_score = 0

        # Dealer cards
        self.dealer_cards = []
        self.dealer_score = 0

        # Variable that stores card images in dict.
        self.card_images = {}

        self.image = image
        self.rect = self.image.get_rect()

        # Position of the cards on the screen
        # Player cards position:
        self.player_cards.rect.midleft  # May have to change 'player_cards', as 
                                        # it's a list. Will only want to show
                                        # cards contained in player hand.

        # Dealer cards position:
        self.dealer_cards.rect.midright  # May have to change 'dealer'_cards',  
                                         # as it's a list. Will only want to 
                                         # show cards contained in dealer hand.
        
        # Store a decimal value for the cards positions (MAY NOT NEED):
        self.x = float(self.rect.x)

    def get_card_image(self):
        for suit in self.suits.values():
            for value in self.values.keys():
                card_name = f'{value}_{suit}'
                folder_name = pg.image.load(f'cards/{card_name}.png')
                self.card_images[card_name] = folder_name
        """
        # Another way to load cards

        card_images_names = ['ace_heart', 'ace_spades', 'ace_club'] # etc
        # a dictionary to store the images with names
        card_images = {}
        # loop through image names, construct the filename and load them as Surfaces
        for name in card_images_names:
            filename = f'cards/{name}.png'
            card_images[name] = pg.image.load(filename).convert()
            
        # Now you have a dictionary of image surfaces that you can blit like this:
        screen.blit(card_images['ace_heart'], (x, y))
        """

        

    def show(self):
        """Placeholder Function
        INCORPORATE BLITME() IF POSSIBLE.
        """
        print(f'{self.values} of {self.suits}')

    # Get cards for both the dealer and player and then show them on screen.
    # ^ Alter blitme method to acommodate this. ^
    def blitme(self):
        """Draws the cards onto the screen."""
        self.screen.blit(self.get_card_image(self.hand), self.rect)





































