from jobe.real.Camera import MowedGrassLine


class RealAI:
    """This is the actual AI for the real-world mower execution"""

    def __init__(self, logger):
        """Set some initial values"""
        self._logger = logger
        self._passing_mode = PassingMode.NotActive

    def should_turn_left(self, camera):
        """This method will determine if the mower should turn left"""

        # If we're passing to left, then try to go around object
        if self._passing_mode == PassingMode.PassingToLeft:
            return True

        # If we're going around and object to right, then stay put
        if self._passing_mode == PassingMode.GoingAroundRight:
            return False

        # If the mowed line is to the left, then try to line it up
        if camera.get_grass_alignment == MowedGrassLine.ToLeftOfMarker:
            self._logger("Alignment is off, turning left")
            return True
        else:
            return False

    def should_turn_right(self, camera):
        """This method will determine if the mower should turn right"""

        # If we're passing to the left, then stay put
        if self._passing_mode == PassingMode.PassingToLeft:
            return False

        # If we're going around an object, turn right
        if self._passing_mode == PassingMode.GoingAroundRight:

            # If we can see mowed grass to right, then we're around the object
            if camera.get_grass_alignment == MowedGrassLine.ToRightOfMarker:
                self._passing_mode = PassingMode.NotActive
                return False

            # If we can see mowed grass to left, then we're around the object
            if camera.get_grass_alignment == MowedGrassLine.ToLeftOfMarker:
                self._passing_mode = PassingMode.NotActive
                return False

            # We can't see mowed grass, so keep turning right
            return True

        # If the mowed line is to the right, then try to line it up
        if camera.get_grass_alignment == MowedGrassLine.ToRightOfMarker:
            self._logger("Alignment is off, turning right")
            return True
        else:
            return False

    def should_move_forward(self, camera):
        """This method will determine if the mower should move forward"""

        # Is there a large object ahead? Then don't move forward
        if camera.large_object_ahead():
            self._logger.write_to_log("Large object ahead")

            # Initiate passing maneuver mode
            self._passing_mode = PassingMode.PassingToLeft
            return False

        # If we're passing and object no longer visible, start to turn back
        if self._passing_mode == PassingMode.PassingToLeft:
            self._passing_mode = PassingMode.GoingAroundRight
            return True

        # If the mowed line is lined up, go straight
        if camera.get_grass_alignment == MowedGrassLine.PerfectlyAligned:
            self._logger.write_to_log("Grass lined up")
            self._passing_mode = PassingMode.NotActive
            return True

        # If the mowed line is not visible, go straight
        elif camera.get_grass_alignment == MowedGrassLine.NotVisible:
            self._logger.write_to_log("Mowed line not visible")
            return True

        # Otherwise, stay put
        else:
            return False

    def should_move_backwards(self, camera):
        """This method will determine if the mower should move backwards"""
        return False


class PassingMode:
    """This class serves as an enum to indicate the mowed grass alignment"""
    PassingToLeft = 0
    GoingAroundRight = 1
    NotActive = 2
