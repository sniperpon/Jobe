class RealAI:
    """This is the actual AI for the real-world mower execution"""

    def __init__(self, logger):
        """Set some initial values"""
        self._logger = logger

    def should_turn_left(self, camera):
        """This method will determine if the mower should turn left"""
        return False

    def should_turn_right(self, camera):
        """This method will determine if the mower should turn right"""
        return False

    def should_move_forward(self, camera):
        """This method will determine if the mower should move forward"""
        return False

    def should_move_backwards(self, camera):
        """This method will determine if the mower should move backwards"""
        return False
