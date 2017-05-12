from jobe.eyes.ShortGrassSide import ShortGrassSide


class SimulationCamera:
    """This is the camera class we will use for simulation mode"""

    def __init__(self, yard):
        """This constructor will initialize the class"""
        self._yard = yard

    def short_grass_in_frame(self):
        """This method will determine if there is short grass visible"""
        return self._yard.is_mower_hitting_mowed_grass()

    def short_grass_lined_up(self):
        """This method will determine if the short grass is lined up"""
        return None

    def large_object_ahead(self):
        """This method will check to see if there is a large object present"""
        return False
