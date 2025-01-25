# This script converts the split pdf pages into images and then performs
# pre-processing on those images.

from pdf2image import convert_from_path
import sys
import os

def pdfsToImages(rawPDFsLocation, outputImageFolder):
    if not os.path.exists(outputImageFolder):
        os.makedirs(outputImageFolder)

    for page in os.listdir(rawPDFsLocation):
        pdfPath = os.path.join(rawPDFsLocation, page)
        pdfName = os.path.splitext(page)[0]
        outputImagePath = os.path.join(outputImageFolder, f'{os.path.splitext(page)[0]}.png')

        try:
            images = convert_from_path(pdfPath)
            for img in enumerate(images): # if dealing with multi-page pdfs, loop over i, img instead of just img ...
                imgPath = f'{outputImagePath[:-4]}.png' # ... and append _[i] after the }.
                img.save(imgPath, 'PNG')

        except Exception as e:
            print(f'Error converting {pdfPath}: e')

        else:
            print(f'Successfully converted {pdfPath} to {outputImagePath}r')

pdfsToImages(sys.argv[1], sys.argv[2])
