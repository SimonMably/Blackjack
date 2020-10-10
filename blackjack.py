import pygame as pg
import random
import sys

from deck import Deck
from card import Card

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
        """
        self.deck = Deck()
        self.card = Card()
        self.dealer = Dealer()
        self.hand = Hand()
        """
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
            # Press 'q' on keyboard to exit the game.
            sys.exit()

if __name__ == '__main__':
    game = Blackjack()
    game.run_game()



