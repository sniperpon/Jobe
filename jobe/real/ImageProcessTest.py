import cv2


# Scenario pictures to test
#   Large object ahead
#   Grass to left of margin line
#   Grass to right of margin line
#   Grass right on margin line
#   Not visible at all

path_prefix = "../../pictures/"


def large_object_ahead():
    """This function will try to recognize a large object in a photograph"""
    image = cv2.imread("large_object.jpg")

    # Return the outcome of our analysis
    return False


# Run our tests
print large_object_ahead()
