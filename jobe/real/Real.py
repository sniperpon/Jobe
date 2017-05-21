class Real:
    """This is the actual driver for the real-world mower execution"""

    def __init__(self, ai, camera, wheels):
        """Set some initial values"""
        self._ai = ai
        self._camera = camera
        self._wheels = wheels
        self._shutoff_cycles = 300

    def run(self):
        """This method contains the actual logic loop"""
        cycles = 0

        while 1:
            cycles += 1

            # We've hit the limit, shut down
            if cycles >= self._shutoff_cycles:
                break

            # Determine our next action
            if self._ai.should_turn_left(self._camera):
                self._wheels.turn_left()
            if self._ai.should_turn_right(self._camera):
                self._wheels.turn_right()
            if self._ai.should_move_forward(self._camera):
                self._wheels.move_forward()
            if self._ai.should_move_backwards(self._camera):
                self._wheels.move_backwards()
