class Camera:
    """This class interfaces with the Raspberry Pi's camera"""

    def __init__(self, logger):
        """Set some initial values"""
        self._logger = logger
