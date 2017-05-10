from jobe.eyes.ShortGrassSide import ShortGrassSide


class Brain:
    """This is the AI class, the brains of the operation"""

    def __init__(self, logger, eyes, legs):
        """This constructor will accept our visitor class instances"""
        self._logger = logger
        self._eyes = eyes
        self._legs = legs
        self._scan_cycles = 0

    def loop(self):
        """This is the main AI loop"""
        if self._scan_cycles >= 256:
            return
        else:
            if self._eyes.short_grass_in_frame():
                if self._eyes.short_grass_lined_up() == ShortGrassSide.Left:
                    self._scan_cycles = 0
                    self._legs.turn_right()
                elif self._eyes.short_grass_lined_up() == ShortGrassSide.Right:
                    self._scan_cycles = 0
                    self._legs.turn_left()
                else:
                    self._scan_cycles += 1
                    self._legs.turn_left()
            else:
                self._legs.go_forward()

            # Restart the loop
            self.loop()
