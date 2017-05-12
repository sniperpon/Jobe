from jobe.eyes.ShortGrassSide import ShortGrassSide


class Brain:
    """This is the AI class, the brains of the operation"""

    def __init__(self, logger, eyes, legs):
        """This constructor will accept our visitor class instances"""
        self._logger = logger
        self._eyes = eyes
        self._legs = legs
        self._scanned_degrees = 0
        self._passing_maneuver = False

    def loop(self):
        """This is the main AI loop"""
        while 1:

            # If we've scanned in all directions and can't find grass, then end
            if self._scanned_degrees >= 360:
                break

            # Is there a large object in our way? Go around it to the right
            if self._eyes.large_object_ahead():
                self._passing_maneuver = True
                self._legs.turn_right()
                self._scanned_degrees += 1
                continue

            # Did we just finish a passing maneuver? Then unwind the scan
            if self._passing_maneuver and self._scanned_degrees > 0:
                self._legs.go_forward()
                self._legs.turn_left()
                self._scanned_degrees -= 1

            # Do we see short grass?
            if self._eyes.short_grass_in_frame():
                self._passing_maneuver = False

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
                self._passing_maneuver = False
                self._legs.go_forward()

        # If we broke out of the loop, then return
        return
