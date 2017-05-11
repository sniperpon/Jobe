import pygame


class Mower(pygame.sprite.Sprite):
    """This class represents the actual lawn mower"""

    def __init__(self, image):
        """This constructor initializes the class"""

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        # Set the image and the initial rectangle
        self._image = image
        self.rect = self._image.get_rect()

        # Set the initial coordinates
        self.set_new_mower_location(0, 0)

    def set_new_mower_location(self, top, left):
        """This method will set the mower to a new spot"""
        image_rect = self._image.get_rect()
        image_rect.top = top
        image_rect.left = left

        # Set the class rectangle to that of the image
        self.rect = image_rect

    def rotate_mower(self, angle):
        """This method will rotate the mower to the desired angle, and will
        return its Surface"""
        return pygame.transform.rotate(self._image, angle)
