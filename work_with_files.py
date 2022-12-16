from PyPDF2 import PdfFileReader
import zipfile
import csv
from openpyxl import load_workbook

# тут только запись в файлы

with zipfile.ZipFile('data/spam.zip', 'w') as myzip:
    myzip.write('data/some.csv')
    myzip.write('data/simple_demo.pdf')
    myzip.write('data/test_with_files.xlsx')  # работа с архивированием в zip


with open('data/some.csv', 'w', newline='') as f:
    state_info = ["California", "Sacramento", "Los Angeles", "39538223"]
    writer = csv.writer(f)
    writer.writerow(state_info)  # работа с csv



pdf_document = "data/simple_demo.pdf"
with open(pdf_document, "rb") as filehandle:
    pdf = PdfFileReader(filehandle)
    info = pdf.getDocumentInfo()
    pages = pdf.getNumPages()
    print(f'\n {info}')
    print(f'\nnumber of pages: {pages}\n') # работа с pdf



