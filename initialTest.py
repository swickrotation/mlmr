import pytesseract
import cv2

# Here we load our data and find some metadata that we will use in
# post-processing in the penultimate block. We also set a base image that we'll
# cut down to size having done out bounding-box magic.

image = cv2.imread("./testImage.png")
im_h, im_w, im_d = image.shape
base_image = image.copy()

# Standard pre-processing of the image. We gray out the image so that we don't
# lose much by way of colour artifacts or weird blending with the colour we're
# setting our bounding boxes, and because image thresholding in opencv expects
# a greyscale image. In our case, the image is going to be purely black and
# white. It's not a photo, so there will be no shadows, and so a binary
# thresholding technique is appropriate. Our blur gives us some leeway around
# the actual text and will be useful in helping us identify the actual contour
# lines later on. Otsu is a magic trick that chooses an optimal image threshold
# on our behalf via some image processing wizardry that I don't pretend to
# have read in detail. Something about finding a minimization in weighted
# variance. Pretty cool.

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]


# We're looking to manipulate the foreground objects, in this case all text.
# It makes good sense then to use rectangles to do our dilation, in this case
# rectangles that are wide and not so tall.

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (20,3))
dilatedImage = cv2.dilate(thresh, kernel, iterations=1)

# Now we find the contours of the particular shape we're trying to capture.
# In this case it's the tiny line separating the footnotes from the main body
# of the text. We use standard elements of the opencv library to do that. The
# lambda is an "anonymous function" that lets us write in-line to sort our
# bounding rectangles first where the number of contours is not 2. Honestly
# I borrowed this part and tweaked it until it worked for my purposes so I need
# to go back and RTFM before I can say I grok this part about actually
# defining the contours. The for-loop I've got well understood tho.

contours = cv2.findContours(dilatedImage, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if len(contours) == 2 else contours[1]
contours = sorted(contours, key=lambda x: cv2.boundingRect(x)[1])
for c in contours:
    x,y,w,h = cv2.boundingRect(c)
    if h < 15 and w > 10:
        roi = base_image[0:y+h - 4, 0:im_w]
        cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0), 2)

cv2.imwrite("temp/output.png", roi)

#ocrSansFootnotes = pytesseract.image_to_string(roi)
#print(ocrSansFootnotes)








