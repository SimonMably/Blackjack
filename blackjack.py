"""The main game file for blackjack."""

import pygame as pg
import random
import sys

from deck import Deck
from card import Card
from player import Player
from dealer import Dealer
from settings import Settings

class Blackjack:
    """Overall class to manage the blackjack game assets and behaviour."""

    def __init__(self):
        """Initialise the game and create game resources."""
        pg.init()

        # Class Attributes
        self.settings = Settings()
        self.card = Card()
        self.player = Player()
        self.dealer = Dealer()
        self.deck = Deck()

        # Display settings (window size, caption and icon)
        self.screen = pg.display.set_mode((self.settings.screen_width, 
                                            self.settings.screen_height))
        pg.display.set_caption("Blackjack")
        
        game_icon = pg.image.load('C:/Users/Simon/Desktop/projects/python_projects/blackjack/images/icons/ace_cards.png')
        pg.display.set_icon(game_icon)
        
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            self.deck.build_deck()  # Check to see if this would print cards in
                                    # cards list (in Deck class)
                                        # 1. Sort out self.suits & self.values
                                        #    in Card class first.

    def _update_screen(self):
        """Updade images on the screen and flip to the new screen."""
        self.screen.fill(self.settings.bg_colour)
        pg.display.flip()
        
    def _check_events(self):
        """Respond to key presses and mouse events."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            
        
        
        
if __name__ == '__main__':
    game = Blackjack()
    game.run_game()