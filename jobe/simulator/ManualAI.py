import pygame


class ManualAI:
    """This class reads keyboard input and returns relevant values"""

    def should_turn_left(self, *args):
        """This method determines if the player wants to turn left"""
        return pygame.key.get_pressed()[pygame.K_LEFT]

    def should_turn_right(self, *args):
        """This method determines if the player wants to turn right"""
        return pygame.key.get_pressed()[pygame.K_RIGHT]

    def should_move_forward(self, *args):
        """This method determines if the player wants to go forward"""
        return pygame.key.get_pressed()[pygame.K_UP]

    def should_move_backwards(self, *args):
        """This method determines if the player wants to go backwards"""
        return pygame.key.get_pressed()[pygame.K_DOWN]
