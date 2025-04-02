import pygame
from pygame.sprite import Sprite
from settings_game_2 import Settings

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, gm_game):
        """Initialize the alien and set its starting position."""
        super().__init__()

        self.screen = gm_game.screen
        self.settings = gm_game.settings
       
        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images_game_2\ship_game_2.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the topright of the screen.
        self.rect.x = self.settings.screen_width - self.rect.height 
        self.rect.y = self.rect.height

        # Store the alien's exact vertical position.
        self.y = float(self.rect.y)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.top <= 0 or self.rect.bottom >= screen_rect.bottom:
            return True
        
    def update(self):
        """Move the alien up or down."""
        self.y += (self.settings.alien_speed *
                   self.settings.fleet_direction)
        self.rect.y = self.y
