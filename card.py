class Card:
    """Class representing the card."""
    
    def __init__(self, image, b_game):
        """Initialise the attributes for the card class."""
        # May need to include the following parameters: image, b_game (game instance)

        self.suits = None  # Replace None with either a dictionary of suits
        self.values = None  # Replace None with a dictionary of values

        self.screen = b_game.screen
        self.settings = b_game.settings
        self.screen_rect = b_game.screen.get_rect()

        # Player cards
        self.player_hand = []
        self.player_score = 0

        # Dealer cards
        self.dealer_hand = []
        self.dealer_score = 0

        # Variable that stores card images in a dictionary.
        self.card_images = {}

        self.image = image
        self.rect = self.image.get_rect()

        # Position of cards on the screen:
        # Player Cards
        self.player_hand.rect.midleft

        # Dealer Cards
        self.dealer_hand.rect.midleft

        self.x = float(self.rect.x)
    
    def get_card_image(self):
        """Get card images and store them somewhere."""
        pass

    def show_cards(self):
        pass