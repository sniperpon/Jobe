import cv2


class MowedGrassLine:
    """This class serves as an enum to indicate the mowed grass alignment"""
    ToRightOfMarker = 0
    ToLeftOfMarker = 1
    PerfectlyAligned = 2
    NotVisible = 3


# Scenario pictures to test
#   Large object ahead
#   Grass to left of margin line
#   Grass to right of margin line
#   Grass right on margin line
#   Not visible at all
#
# Conjecture
#   Might be able to use this for large objects, like trees, the kids, dogs:
#       docs.opencv.org/2.4/modules/objdetect/doc/cascade_classification.html
#   Maybe can use this for the grass detection?
#       https://en.wikipedia.org/wiki/Canny_edge_detector

path_prefix = "../../pictures/TestImages/"


def large_object_ahead():
    """This function will try to recognize a large object in a photograph"""
    image = cv2.imread("large_object.jpg")

    # Return the outcome of our analysis
    return False


def get_grass_alignment():
    """This function will return how the grass is aligned"""

    # Always return false for the moment
    return MowedGrassLine.NotVisible


def fast_feature_test():
    """This function will test the FAST feature detection"""
    img = cv2.imread("Mowed_Aligned_01.jpg", 0)

    # Initiate FAST object with default values
    fast = cv2.FastFeatureDetector()

    # Find and draw the keypoints
    kp = fast.detect(img, None)
    img2 = cv2.drawKeypoints(img, kp, color=(255, 0, 0))

    # Print all default params
    print "Threshold: ", fast.getInt("threshold")
    print "nonmaxSuppression: ", fast.getBool("nonmaxSuppression")
    print "neighborhood: ", fast.getInt("type")
    print "Total Keypoints with nonmaxSuppression: ", len(kp)

    cv2.imwrite("fast_true.png", img2)

    # Disable nonmaxSuppression
    fast.setBool("nonmaxSuppression", 0)
    kp = fast.detect(img, None)

    print "Total Keypoints without nonmaxSuppression: ", len(kp)

    img3 = cv2.drawKeypoints(img, kp, color=(255, 0, 0))

    cv2.imwrite("fast_false.png", img3)


# Run our tests
print large_object_ahead()
print get_grass_alignment()
