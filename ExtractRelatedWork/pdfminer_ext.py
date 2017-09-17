from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import sys

def convert(infile):
    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, codec='utf-8', laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)
    
    for page in PDFPage.get_pages(infile):
        interpreter.process_page(page)
    converter.close()
    text = output.getvalue()
    output.close
    return text 

fname = sys.argv[1]
fname = 'test.pdf'
infile = open(fname, 'rb')

convert(infile, 1)

infile.close()
