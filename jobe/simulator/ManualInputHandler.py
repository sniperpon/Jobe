import pygame


class ManualInputHandler:
    """This class reads keyboard input and returns relevant values"""

    def turn_left(self):
        """This method determines if the player wants to turn left"""
        return pygame.key.get_pressed()[pygame.K_LEFT]

    def turn_right(self):
        """This method determines if the player wants to turn right"""
        return pygame.key.get_pressed()[pygame.K_RIGHT]

    def move_forward(self):
        """This method determines if the player wants to go forward"""
        return pygame.key.get_pressed()[pygame.K_UP]

    def move_backwards(self):
        """This method determines if the player wants to go backwards"""
        return pygame.key.get_pressed()[pygame.K_DOWN]
