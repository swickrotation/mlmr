import cv2
import os

'''
In order to make the OCR most effective, we need to pre-process the data. 
There are a few standard operations to perform, including re-sizing,
de-noising, thresholding , and grayscaling. We do all of this below.
'''

inputDir = '../trainingData/pagesAsImages/'
outputDir ='../trainingData/preprocessedPageImages/' 


def imagePreprocess(inputPath, outputPath):
    os.makedirs(os.path.dirname(outputPath), exist_ok=True)
    image = cv2.imread(inputPath)

    # First step: Convert to pure grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    '''
     Next we apply a median blur - this will help wipe away noise without
     affecting the computer's ability to read. Always useful to remember: they
     don't see like we see. Median blurs are a little more intensive but
     do a better job at edge preservation. We want good edge preservation so we
     don't lose tables or footnote demarkations.
    '''
    medianBlur = cv2.medianBlur(gray, 3)

    '''
    There are quite a few approaches to binarization but Otsu's method is
    considered among the best. We'll use it for now, unless adaptive gaussian
    thresholding starts to seem better.
    '''
    ret, binary = cv2.threshold(medianBlur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # This utility does edge detection. Will probably need to tune this by hand.
    # May not be necessary at all.
    #edges = cv2.Canny(binary, 50, 150)

    # improve connectivity / remove small artifacts
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2))
    #
    dilated = cv2.dilate(binary, kernel, iterations = 1)
    # 
    # eroded = cv2.erode(edges, kernel, iterations = 1)

    # I've seen it suggested that resizing can help OCR accuracy. Let's see.
    resized = cv2.resize(dilated, None, fx=2, fy=2, interpolation= cv2.INTER_LINEAR)
    #resizedEdges = cv2.resize(edges, None, fx=2, fy=2, interpolation= cv2.INTER_LINEAR)

    cv2.imwrite(f'{outputPathBase}.png', resized)
    #cv2.imwrite(f'{outputPathBase}_edges.png', resizedEdges)

for image in os.listdir(inputDir):
    inputPath = os.path.join(inputDir, image)
    outputPathBase = os.path.join(outputDir, f"preprocessed_{os.path.splitext(image)[0]}")
    imagePreprocess(inputPath, outputPathBase)
    print(f'Processed and saved: {outputPathBase}.png')# and {outputPathBase}_edges.png')
print("Batch Preprocessing Complete")
