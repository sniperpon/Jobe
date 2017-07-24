import pygame


class AutomaticAI:
    """This class reads keyboard input and returns relevant values"""

    def __init__(self, logger):
        """Set some initial values"""
        self._logger = logger
        self._safe_threshold = 8
        self._current_safe = 0

    def should_turn_left(self, mower, obstacles):
        """This method determines if the player wants to turn left"""
        self._mower_colliding(mower, obstacles)
        self._logger.write_to_log("Mower deg: " + str(mower.degrees))

        # If we're colliding, turn left
        if self._mower_colliding(mower, obstacles):
            return True
        else:
            return False

    def should_turn_right(self, mower, obstacles):
        """This method determines if the player wants to turn right"""
        self._mower_colliding(mower, obstacles)
        self._logger.write_to_log("Mower deg: " + str(mower.degrees))

        # If we're in the free and clear, turn right to look for long grass
        if self._free():
            return True
        else:
            return False

    def should_move_forward(self, mower, obstacles):
        """This method determines if the player wants to go forward"""
        self._mower_colliding(mower, obstacles)
        self._logger.write_to_log(
            "Mower pos: " + str(mower.left) + " x " + str(mower.top)
        )

        # Keep forging ahead
        return True

    def should_move_backwards(self, mower, obstacles):
        """This method determines if the player wants to go backwards"""
        self._mower_colliding(mower, obstacles)
        self._logger.write_to_log(
            "Mower pos: " + str(mower.left) + " x " + str(mower.top)
        )

        # At the moment, don't ever go backwards
        return False

    def _mower_colliding(self, mower, obstacles):
        """This method determines of the mower is colliding"""
        if len(pygame.sprite.spritecollide(mower, obstacles, False)):
            self._current_safe = 0
            return True
        else:
            self._current_safe += 1
            return False

    def _free(self):
        """This method determines of the mower is free and clear"""
        return self._current_safe >= self._safe_threshold
