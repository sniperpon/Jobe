import math


class SimulationMover:
    """This is the movement class we will use for simulation mode"""

    def __init__(self, yard):
        """This constructor will initialize the class"""
        self._yard = yard
        self._mower_x = 256
        self._mower_y = 64
        self._mower_angle = 270

        # Render the board, initially
        self._yard.draw_yard(
            self._mower_x,
            self._mower_y,
            self._mower_angle,
            True
        )

    def go_forward(self):
        """This method will move the robot forward"""

        # Determine the new X and Y coordinates
        radians = math.radians(self._mower_angle)
        self._mower_x += math.cos(radians)
        self._mower_y += math.sin(radians)

        # Re-draw the yard now that we've moved
        self._yard.draw_yard(
            self._mower_x,
            self._mower_y,
            self._mower_angle
        )

    def go_backwards(self):
        """This method will move the robot backwards"""

        # Determine the new X and Y coordinates
        radians = math.radians(self._mower_angle)
        self._mower_x -= math.cos(radians)
        self._mower_y -= math.sin(radians)

        # Re-draw the yard now that we've moved
        self._yard.draw_yard(
            self._mower_x,
            self._mower_y,
            self._mower_angle
        )

    def turn_left(self):
        """This method will turn the robot to the left"""
        self._mower_angle -= 90

        # Re-draw the yard now that we've moved
        self._yard.draw_yard(
            self._mower_x,
            self._mower_y,
            self._mower_angle
        )

    def turn_right(self):
        """This method will turn the robot to the right"""
        self._mower_angle += 90

        # Re-draw the yard now that we've moved
        self._yard.draw_yard(
            self._mower_x,
            self._mower_y,
            self._mower_angle
        )

    def stop(self):
        """This method will stop the robot"""
        self._yard.draw_yard(
            self._mower_x,
            self._mower_y,
            self._mower_angle
        )
