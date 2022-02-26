import pygame

class Stars():
    """A class to manage the stars."""

    def __init__(self, ai_game):
        """Create a stars object."""
        self.screen = ai_game.screen

        # Load the stars image and get its rect.
        self.stars = pygame.image.load('images/stars.bmp')
        self.rect = self.stars.get_rect()

        self.rect.x = 1700
        self.rect.y = 60

    def blitme(self):
        """Draw the stars."""
        self.screen.blit(self.stars, self.rect)