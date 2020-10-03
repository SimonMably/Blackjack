import pygame as pg
import random
import sys


# Game Settings
# Screen dimensions:
S_HEIGHT = 750
S_WIDTH = 1200


# Background colour:
BG_COLOUR = (0, 255, 0)

class blackjack:
    """Overal class to manage the blackjack game assetts and behaviour."""

    def __init__(self):
        """Initialise the game and create game resources."""
        pg.init()

        self.screen = pg.display.set_mode((S_HEIGHT, S_WIDTH))
        pg.display.set_caption("Blackjack")

        pg.display.update()

    def run_game(self):
        self._update_screen()


    def _update_screen(self):
        """Update images ont he screen and flip to the new screen."""
        self.screen.fill(BG_COLOUR)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        pass

    def _check_keydown_events(self, events):
        """Respond to keypresses."""
        pass

class Card:
    """A class that manages each card."""
    pass


class Deck:
    """A class that manages each card."""
    pass






if __name__ == '__main__':
    game = blackjack()
    game.run_game()



