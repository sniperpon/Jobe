import pygame


class ManualAI:
    """This class reads keyboard input and returns relevant values"""

    def __init__(self, logger):
        """Set some initial values"""
        self._logger = logger

    def should_turn_left(self, mower, obstacles):
        """This method determines if the player wants to turn left"""
        self._logger.write_to_log("Mower deg: " + str(mower.degrees))
        return pygame.key.get_pressed()[pygame.K_LEFT]

    def should_turn_right(self, mower, obstacles):
        """This method determines if the player wants to turn right"""
        self._logger.write_to_log("Mower deg: " + str(mower.degrees))
        return pygame.key.get_pressed()[pygame.K_RIGHT]

    def should_move_forward(self, mower, obstacles):
        """This method determines if the player wants to go forward"""
        self._logger.write_to_log(
            "Mower pos: " + str(mower.left) + " x " + str(mower.top)
        )
        return pygame.key.get_pressed()[pygame.K_UP]

    def should_move_backwards(self, mower, obstacles):
        """This method determines if the player wants to go backwards"""
        self._logger.write_to_log(
            "Mower pos: " + str(mower.left) + " x " + str(mower.top)
        )
        return pygame.key.get_pressed()[pygame.K_DOWN]
