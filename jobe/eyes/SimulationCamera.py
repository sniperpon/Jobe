from jobe.eyes.ShortGrassSide import ShortGrassSide


class SimulationCamera:
    """This is the camera class we will use for simulation mode"""

    def short_grass_in_frame(self):
        """This method will determine if there is short grass visible"""
        return ShortGrassSide.Left

    def short_grass_lined_up(self):
        """This method will determine if the short grass is lined up"""
        return True
