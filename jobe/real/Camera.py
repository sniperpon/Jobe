import picamera
import cv2
from io import BytesIO


class Camera:
    """This class interfaces with the Raspberry Pi's camera"""
    # http://picamera.readthedocs.io/en/release-1.13/recipes1.html
    # http://www.learnopencv.com

    def __init__(self, logger):
        """Set some initial values"""
        self._logger = logger
        self._camera = picamera.PiCamera()

    def large_object_ahead(self):
        """This method will determine if there is a large object in frame"""

        # Always return false for the moment
        return False

    def get_grass_alignment(self):
        """This method will return how the grass is aligned"""

        # Always return false for the moment
        return MowedGrassLine.NotVisible

    def _take_picture(self):
        """This method will return the handle to a fresh picture"""
        file_handle = open("pictures/current.jpg", "wb")

        # Capture the image into our file handle, then close the handle
        self._camera.capture(file_handle)
        file_handle.close()


class MowedGrassLine:
    """This class serves as an enum to indicate the mowed grass alignment"""
    ToRightOfMarker = 0
    ToLeftOfMarker = 1
    PerfectlyAligned = 2
    NotVisible = 3
