from PIL import Image
import cv2
import pytesseract


# The image "testImage.png" is located in the same directory as the code being
# ran. This names the image for further use with the PIL function Image, and
# demonstrates the placement of the testfile within our coding framework.

testImage = "./testImage.png"

# This block opens the image for our initial analysis. The first line assigns
# a shorthand for the testimage as it is being interpreted by PIL's Image
# function. The second line prints interesting and potentially useful metadata.
# The third opens the image in the default image viewer.

im = Image.open(testImage)
print (im)
#im.show()

# Now we take care of rotations in the page.

import numpy as np
