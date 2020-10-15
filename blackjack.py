import pygame as pg
import random
import sys

from deck import Deck
from card import Card
from player import Player

# Main Game File.

# -----------------------------------------------------------------------------

# Game Settings
# Screen dimensions:
S_HEIGHT = 750
S_WIDTH = 1200

# Background colour:
BG_COLOUR = (0, 150, 0)

# -----------------------------------------------------------------------------

class Blackjack:
    """Overal class to manage the blackjack game assetts and behaviour."""

    def __init__(self):
        """Initialise the game and create game resources."""
        pg.init()

        self.screen = pg.display.set_mode((S_WIDTH, S_HEIGHT))
        pg.display.set_caption("Blackjack")

        self.deck = Deck()
        self.card = Card()
        self.player = Player()

        pg.display.update()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()

    def _update_screen(self):
        """Update images ont he screen and flip to the new screen."""
        self.screen.fill(BG_COLOUR)
        pg.display.flip()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pg.K_q:
            ### Add a feature that gets game to ask the user if they really want
            ### to quit. Implement using an if statement. 
            ### (This is a precaution - in case user presses the 'q' key 
            ### accidentally)
 
            # Press 'q' on keyboard to exit the game.
            sys.exit()

if __name__ == '__main__':
    game = Blackjack()
    game.run_game()



