class RealCamera:
    """This is the camera class we will use for real mode"""

    def short_grass_in_frame(self):
        """This method will determine if there is short grass visible"""
        return True

    def short_grass_lined_up(self):
        """This method will determine if the short grass is lined up"""
        return True

    def large_object_ahead(self):
        """This method will check to see if there is a large object present"""
        return False
