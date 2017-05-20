import pygame


class Grass(pygame.sprite.Sprite):
    """This class represents the grass within the yard"""

    def __init__(self, width, height):
        """This constructor prepares our grass"""
        pygame.sprite.Sprite.__init__(self)

        # Prepare the grass for rendering
        color = pygame.Color(0, 135, 38, 255)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
