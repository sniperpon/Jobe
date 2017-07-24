import pygame
import math


class Mower(pygame.sprite.Sprite):
    """This class represents a lawn mower"""

    def __init__(self, left, top, degrees, speed):
        """This constructor will prepare the mower for usage"""
        pygame.sprite.Sprite.__init__(self)

        # Degrees: 0 is right, 90 degrees is down, 180 is left, 270 is up
        self.left = left
        self.top = top
        self.degrees = degrees
        self._speed = speed

        # Prepare the mower for rendering
        self._orig_image = pygame.image.load("jobe/resources/Arrow.png")
        self._orig_image = self._orig_image.convert_alpha()
        self.image = self._orig_image
        self.rect = self.image.get_rect()
        self._undo_method = None

    def update(self, obstacles):
        """This method is called by pygame's group, each frame"""
        self.rect.center = (self.left, self.top)

        # Are we colliding with a tree? Then undo our last action
        if (
            self._undo_method is not None
            and len(pygame.sprite.spritecollide(self, obstacles, False)) > 0
        ):
            self._undo_method()

    def rotate_ccw(self):
        """This method will adjust the degrees counter clockwise"""
        self.degrees -= self._speed

        # If the degrees become less than 0, reset them to 360
        if self.degrees <= 0:
            self.degrees = 360

        # Rotate the image
        self.image = pygame.transform.rotate(
            self._orig_image,
            (self.degrees - 270) * -1)

        # How would we undo this?
        self._undo_method = self.rotate_cw

    def rotate_cw(self):
        """This method will adjust the degrees clockwise"""
        self.degrees += self._speed

        # If the degrees become greater than 360, reset them to zero
        if self.degrees >= 360:
            self.degrees = 0

        # Rotate the image
        self.image = pygame.transform.rotate(
            self._orig_image,
            (self.degrees - 270) * -1)

        # How would we undo this?
        self._undo_method = self.rotate_ccw

    def forward(self):
        """This method will adjust the mower's position, forward once"""
        radians = math.radians(self.degrees)

        # Set the new left and top positions, using... maths...
        for x in range(0, self._speed):
            self.left += math.cos(radians)
            self.top += math.sin(radians)

        # How would we undo this?
        self._undo_method = self.backwards

    def backwards(self):
        """This method will adjust the mower's position, backwards once"""
        radians = math.radians(self.degrees)

        # Set the new left and top positions, using... maths...
        for x in range(0, self._speed):
            self.left -= math.cos(radians)
            self.top -= math.sin(radians)

        # How would we undo this?
        self._undo_method = self.forward
