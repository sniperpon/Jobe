import pygame


class Grass(pygame.sprite.Sprite):
    """This class represents the grass within the yard"""

    def __init__(self, left, top, width, height, grass_type):
        """This constructor prepares our grass"""
        pygame.sprite.Sprite.__init__(self)

        # Set some values
        color = None
        self._grass_type = grass_type
        self._left = left
        self._top = top

        # Determine the grass color
        if self._grass_type == GrassType.Tall:
            color = pygame.Color(0, 135, 38, 255)
        elif self._grass_type == GrassType.Short:
            color = pygame.Color(0, 201, 57, 255)

        # Prepare the image for rendering
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def update(self):
        """This method is called by pygame's group, each frame"""
        if self._grass_type == GrassType.Short:
            self.rect.center = (self._left, self._top)


class GrassType:
    """This class serves as an enum to indicate grass type"""
    Tall = 0
    Short = 1
