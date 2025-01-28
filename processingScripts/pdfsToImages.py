# This script converts the split pdf pages into images. For now I'm going to
# do the pre-processing in another script but we'll put them together later.


from pdf2image import convert_from_path
import sys
import os

def pdfToPNG(inputPath, outputPath):
    os.makedirs(outputPath, exist_ok=True)

    for page in os.listdir(inputPath):
        pdfPath = os.path.join(inputPath, page)
        outputImage = os.path.join(outputPath, f'{os.path.splitext(page)[0]}.png')

        images = convert_from_path(pdfPath)
        for img in images:
            img.save(outputImage, 'PNG')

pdfToPNG(sys.argv[1], sys.argv[2])
