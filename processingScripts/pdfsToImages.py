# This script converts the split pdf pages into images. For now I'm going to
# do the pre-processing in another script but we'll put them together later.


from pdf2image import convert_from_path
import sys
import os

def pdfToPNG(inputDir, outputDir):
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)  

    for page in os.listdir(inputDir):
        pdfPath = os.path.join(inputDir, page)
        outputImage = os.path.join(outputDir, f'{os.path.splitext(page)[0]}.png')
        #print(outputImage)

        images = convert_from_path(pdfPath)
        for img in images:
            img.save(outputImage, 'PNG')

pdfToPNG(sys.argv[1], sys.argv[2])
