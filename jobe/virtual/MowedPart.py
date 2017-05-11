import pygame


class MowedPart(pygame.sprite.Sprite):
    """This class represents a mowed part of grass"""

    def __init__(self, color, top, left, width, height):
        """This constructor initializes the class"""

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        # Create an image, fill it in, and set its coordinates
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        image_rect = self.image.get_rect()
        image_rect.top = top
        image_rect.left = left

        # Set the class rectangle to that of the image
        self.rect = image_rect
