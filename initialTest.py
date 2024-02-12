from PIL import Image
import cv2
import pytesseract
import numpy as np


# The image "testImage.png" is located in the same directory as the code being
# ran. This names the image for further use with the PIL function Image, and
# demonstrates the placement of the testfile within our coding framework.

testImage = "./testImage.png"

# This block opens the image for our initial analysis. The first line assigns
# a shorthand for the testimage as it is being interpreted by PIL's Image
# function. The second line prints interesting and potentially useful metadata.
# The third opens the image in the default image viewer.

#image = Image.open(testImage)
#print (image)
#im.show()

# If we were preprocessing the image, this is where we would take care of
# that. In our case there aren't noticeable artifacts so we can forget about
# that for now. Likely pre-processing would include removing artifacts and
# correcting page alignment.

'''

SPACE LEFT INTENTIONALLY BLANK --- ROOM FOR IMAGE PREPROCESSING

'''

# Now we begin our process of eliminating footnotes. First we check to see that
# the OCR actually reads text from our image:

#ocrNoPreProcess = pytesseract.image_to_string(image)
#print (ocrNoPreProcess)

# and we see that it does. Now we can set up our bounding boxes: first, we
# blur the image to outline the forms of the textblocks on the page. Then we 
# set a threshold of black and white to improve the contrast and make those 
# blurred blocks look as distinct as possible.

image = cv2.imread("./testImage.png")
blur = cv2.GaussianBlur(image, (7,7), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# now we apply a kernel filtering to the result so that tesseract can easily
# identify the regions.

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 3))
dilate = cv2.dilate(thresh, kernel, iterations=1)
cv2.imwrite("temp/sample_blur.png", blur)
cv2.imwrite("temp/sample_dilated.png", dilate)

# Now we find the contours:

contours = cv2.FindContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if len(contours) == 2 else contours[1]
contours = sorted(contours, key=lambda x: cv2.boundingRect(x)[1])

for c in contours:
    x,y,w,h = cv2.boundingRect(c)
    if h > 100 and w > 150
        cv2.rectangle(image, (x,y), (x+w, y+h), (36,255,12), 2)

cv2.imwrite("temp/boxTest.png", image)
