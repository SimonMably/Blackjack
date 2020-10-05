import pygame as pg
import random
import sys

from hand import Hand
from deck import Deck
from dealer import Dealer

# Game Settings
# Screen dimensions:
S_HEIGHT = 750
S_WIDTH = 1200

# Background colour:
BG_COLOUR = (0, 150, 0)

class Blackjack:
    """Overal class to manage the blackjack game assetts and behaviour."""

    def __init__(self):
        """Initialise the game and create game resources."""
        pg.init()

        self.screen = pg.display.set_mode((S_WIDTH, S_HEIGHT))
        pg.display.set_caption("Blackjack")

        pg.display.update()
        


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            self.blitme(self.playing_deck)
            """
            self.playing_deck = [
                ("Ace of Hearts", 11, "images/cards/ace_hearts.png"), \
                ("2 of Hearts", 2, "images/cards/two_hearts.png"), \
                ("3 of Hearts", 3, "images/cards/three_hearts.png"), \
                ("4 of Hearts", 4, "images/cards/four_hearts.png"), \
                ("5 of Hearts", 5, "images/cards/five_hearts.png"), \
                ("6 of Hearts", 6, "images/cards/six_hearts.png"), \
                ("7 of Hearts", 7, "images/cards/seven_hearts.png"), \
                ("8 of Hearts", 8, "images/cards/eight_hearts.png"), \
                ("9 of Hearts", 9, "images/cards/nine_hearts.png"), \
                ("10 of Hearts", 10, "images/cards/ten_hearts.png"), \
                ("Jack of Hearts", 10, "images/cards/jack_hearts.png"), \
                ("Queen of Hearts", 10, "images/cards/queen_hearts.png"), \
                ("King of Hearts", 10, "images/cards/king_hearts.png"), \
                ("Ace of Spades", 11, "images/cards/ace_spades.png"), \
                ("2 of Spades", 2, "images/cards/two_spades.png"), \
                ("3 of Spades", 3, "images/cards/three_spades.png"), \
                ("4 of Spades", 4, "images/cards/four_spades.png"), \
                ("5 of Spades", 5, "images/cards/five_spades.png"), \
                ("6 of Spades", 6, "images/cards/six_spades.png"), \
                ("7 of Spades", 7, "images/cards/seven_spades.png"), \
                ("8 of Spades", 8, "images/cards/eight_spades.png"), \
                ("9 of Spades", 9, "images/cards/nine_spades.png"), \
                ("10 of Spades", 10, "images/cards/ten_spades.png"), \
                ("Jack of Spades", 10, "images/cards/jack_spades.png"), \
                ("Queen of Spades", 10, "images/cards/queen_spades.png"), \
                ("King of Spades", 10, "images/cards/king_spades.png"), \
                ("Ace of Diamonds", 11, "images/cards/ace_diamonds.png"), \
                ("2 of Diamonds", 2, "images/cards/two_diamonds.png"), \
                ("3 of Diamonds", 3, "images/cards/three_diamonds.png"), \
                ("4 of Diamonds", 4, "images/cards/four_diamonds.png"), \
                ("5 of Diamonds", 5, "images/cards/five_diamonds.png"), \
                ("6 of Diamonds", 6, "images/cards/six_diamonds.png"), \
                ("7 of Diamonds", 7, "images/cards/seven_diamonds.png"), \
                ("8 of Diamonds", 8, "images/cards/eight_diamonds.png"), \
                ("9 of Diamonds", 9, "images/cards/nine_diamonds.png"), \
                ("10 of Diamonds", 10, "images/cards/ten_diamonds.png"), \
                ("Jack of Diamonds", 10, "images/cards/jack_diamonds.png"), \
                ("Queen of Diamonds", 10, "images/cards/queen_diamonds.png"), \
                ("King of Diamonds", 10, "images/cards/king_diamonds.png"), \
                ("Ace of Clubs", 11, "images/cards/ace_clubs.png"), \
                ("2 of Clubs", 2, "images/cards/two_clubs.png"), \
                ("3 of Clubs", 3, "images/cards/three_clubs.png"), \
                ("4 of Clubs", 4, "images/cards/four_clubs.png"), \
                ("5 of Clubs", 5, "images/cards/five_clubs.png"), \
                ("6 of Clubs", 6, "images/cards/six_clubs.png"), \
                ("7 of Clubs", 7, "images/cards/seven_clubs.png"), \
                ("8 of Clubs", 8, "images/cards/eight_clubs.png"), \
                ("9 of Clubs", 9, "images/cards/nine_clubs.png"), \
                ("10 of Clubs", 10, "images/cards/ten_clubs.png"), \
                ("Jack of Clubs", 10, "images/cards/jack_clubs.png"), \
                ("Queen of Clubs", 10, "images/cards/queen_clubs.png"), \
                ("King of Clubs", 10, "images/cards/king_clubs.png")]
            """
            player_hand = []
            player_score = 0
            dealer_hand = []
            dealer_score = 0

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

    def blitme(self):
        self.screen.blit(self.playing_deck)


class Card:
    """A class that manages each card."""
    pass


class Deck:
    """A class that manages each card."""
    pass


if __name__ == '__main__':
    game = Blackjack()
    game.run_game()



