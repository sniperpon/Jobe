class SimulationMover:
    """This is the movement class we will use for simulation mode"""

    def __init__(self, yard):
        """This constructor will initialize the class"""
        self._yard = yard

        # Render the board, initially
        self._yard.draw_yard()

    def go_forward(self):
        """This method will move the robot forward"""

        # Re-draw the yard now that we've moved
        self._yard.draw_yard()

    def turn_left(self):
        """This method will turn the robot to the left"""

    def turn_right(self):
        """This method will turn the robot to the right"""

    def stop(self):
        """This method will turn the robot to the right"""
