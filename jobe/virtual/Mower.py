import pygame
import math


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

    def get_trail_spot(self, angle):
        """This method will return the X and Y coordinates of where the
        mower just mowed"""
        radians = math.radians(angle)
        x_value = self.rect.left + (math.cos(radians))
        y_value = self.rect.top + (math.sin(radians))

        # Return our value
        return x_value, y_value

    def set_new_mower_location(self, top, left):
        """This method will set the mower to a new spot"""
        image_rect = self._image.get_rect()
        image_rect.top = top
        image_rect.left = left

        # Set the class rectangle to that of the image
        self.rect = image_rect

    def rotate_mower(self, top, left, angle):
        """This method will rotate the mower to the desired angle, and will
        return its Surface"""
        self.set_new_mower_location(top, left)

        # Do some fancy work to rotate without the image distorting
        original_rect = self._image.get_rect()
        rotated_image = pygame.transform.rotate(self._image, angle)
        rotated_rect = original_rect.copy()
        rotated_rect.center = rotated_image.get_rect().center
        return rotated_image.subsurface(rotated_rect).copy()
