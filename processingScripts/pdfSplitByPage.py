#!/usr/bin/env/python3

# This script takes a pdf input and outputs the pages of the input as their
# own pdfs. I wrote it to split up mecwv01 so that we can use the pages of
# that document as training data for the OCR model. Requires manual entry of
# input pdf and output destination. Script will name outputs automatically, by
# page. -W

from PyPDF2 import PdfWriter, PdfReader
import sys
import re
import os

def pdfSplitByPage(inputFile, outputPath):
    os.makedirs(outputPath, exist_ok=True)
    inputpdf = PdfReader(open(inputFile, 'rb'))
    for i in range (len(inputpdf.pages)):
        output = PdfWriter()
        output.add_page(inputpdf.pages[i])
        outputPreName = inputFile.split('/')[-1]
        outputPreName = re.sub('\.pdf$', '', outputPreName)
        if 0<= i < 9:
            with open(outputPath + outputPreName + '_00%s.pdf' %(i+1), 'wb') as outputPage:
                output.write(outputPage)
        elif 9 <= i < 99:
            with open(outputPath + outputPreName + '_0%s.pdf' %(i+1), 'wb') as outputPage:
                output.write(outputPage)
        else:
            with open(outputPath + outputPreName + '_%s.pdf' %(i+1), 'wb') as outputPage:
                output.write(outputPage)
pdfSplitByPage(sys.argv[1], sys.argv[2])
# fisrt argument should be the file you wish to split, second argument the
# directory in which you would like to save the output.
