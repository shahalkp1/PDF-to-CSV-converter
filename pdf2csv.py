import os
import re
import csv
def cleanlines(value):
	value = value.strip()
	return ''.join(value.splitlines())
def clean(text):
  txt=text.replace('\n', ' ')
  txt=txt.replace('\t', ' ')
  txt = re.sub('[^a-zA-Z0-9 \n\.]', ' ',txt)
  txt=txt.strip()
  txt=cleanlines(txt)
  return txt
def pdf_to_txt(path):
    from io import StringIO
    from pdfminer.converter import TextConverter
    from pdfminer.layout import LAParams
    from pdfminer.pdfdocument import PDFDocument
    from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
    from pdfminer.pdfpage import PDFPage
    from pdfminer.pdfparser import PDFParser

    output_string = StringIO()
    with open(path, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
    text = str(output_string.getvalue())
    return text
list=[]
directory = r'InputDir'
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        pdfminersix_test = pdf_to_txt(f)
        pdfminersix_test=clean(pdfminersix_test)
        list.append([pdfminersix_test])
with open(r'OutputDir.csv', 'w+', newline ='') as f: 
    write = csv.writer(f) 
    #write.writerow('Data')
    write.writerows(list) 
