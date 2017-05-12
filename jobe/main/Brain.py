from jobe.eyes.ShortGrassSide import ShortGrassSide


class Brain:
    """This is the AI class, the brains of the operation"""

    def __init__(self, logger, eyes, legs):
        """This constructor will accept our visitor class instances"""
        self._logger = logger
        self._eyes = eyes
        self._legs = legs
        self._scanned_degrees = 0

    def loop(self):
        """This is the main AI loop"""
        if self._scanned_degrees >= 360:
            return
        else:
            # Do we see short grass?
            if self._eyes.short_grass_in_frame():

                # Is the grass to the right of our offset? Turn to line it up
                if self._eyes.short_grass_lined_up() == ShortGrassSide.Right:
                    self._scanned_degrees = 0
                    self._legs.turn_right()

                # Is the grass to the left of our offset? Turn to line it up
                elif self._eyes.short_grass_lined_up() == ShortGrassSide.Left:
                    self._scanned_degrees = 0
                    self._legs.turn_left()

                # We're lined up! Move forward
                elif self._eyes.short_grass_lined_up() == ShortGrassSide.Good:
                    self._legs.go_forward()

                # Something happened; back up, and start scanning for grass
                else:
                    self._scanned_degrees += 1
                    self._legs.go_backwards()
                    self._legs.turn_left()

            # We don't see any short grass; move forward
            else:
                self._legs.go_forward()

        # Restart the loop!
        self.loop()
