from jobe.thunderborg.ThunderBorg import ThunderBorg


class Wheels:
    """This class interfaces with the robot's wheels"""
    # https://www.piborg.org/thunderborg/install

    def __init__(self, logger):
        """Set some initial values"""
        self._logger = logger
        self._speed = 20

        # Initialize the motor controller boards
        self._front_board = self._prepare_board(10)
        self._rear_board = self._prepare_board(11)

    def turn_left(self):
        """Turn the mower to the left"""
        self._front_board.SetMotor1(self._speed * -1)
        self._front_board.SetMotor2(self._speed)
        self._rear_board.SetMotor1(self._speed * -1)
        self._rear_board.SetMotor2(self._speed)
        self._front_board.MotorsOff()

    def turn_right(self):
        """Turn the mower to the right"""
        self._front_board.SetMotor1(self._speed)
        self._front_board.SetMotor2(self._speed * -1)
        self._rear_board.SetMotor1(self._speed)
        self._rear_board.SetMotor2(self._speed * -1)
        self._front_board.MotorsOff()

    def move_forward(self):
        """Move the mower forward"""
        self._front_board.SetMotor1(self._speed)
        self._front_board.SetMotor2(self._speed)
        self._rear_board.SetMotor1(self._speed)
        self._rear_board.SetMotor2(self._speed)
        self._front_board.MotorsOff()

    def move_backwards(self):
        """Move the mower backwards"""
        self._front_board.SetMotor1(self._speed * -1)
        self._front_board.SetMotor2(self._speed * -1)
        self._rear_board.SetMotor1(self._speed * -1)
        self._rear_board.SetMotor2(self._speed * -1)
        self._front_board.MotorsOff()

    @staticmethod
    def _prepare_board(address):
        """This helper method initializes a motor controller"""
        board = ThunderBorg()
        board.i2cAddress = address
        board.Init()

        # Return the ThunderBorg instance to the caller
        return board
