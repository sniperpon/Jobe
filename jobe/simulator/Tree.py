import pygame


class Tree(pygame.sprite.Sprite):
    """This class represents a tree"""

    def __init__(self, left, top):
        """This constructor will prepare the tree for usage"""
        pygame.sprite.Sprite.__init__(self)

        # Set the tree's location
        self._left = left
        self._top = top

        # Load the image and set the rectangle
        self.image = pygame.image.load("jobe/resources/Tree.png")
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()

    def update(self):
        """This method is called by pygame's group, each frame"""
        self.rect.center = (self._left, self._top)
