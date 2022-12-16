import os.path
import re
from PyPDF2 import PdfFileReader
import zipfile
import csv
from openpyxl import load_workbook

# тут только тесты с файлами

# я не знаю почему но пока не заранить work_with_files она не будет читать его здесь
with zipfile.ZipFile('data/spam.zip', 'r') as myzip:
    print(' В архив входят:')
    for name in myzip.namelist():  # читаем файл
        print(os.path.relpath(name, 'data/'))
    len(myzip.namelist())

    if len(myzip.namelist()) == 3:  # проверка сколько файлов входтит в файл
        print("\nTrue")
    else:
        print('\nFalse')
        print(len(myzip.namelist()))

    # тут проверка какие файлы входят в архив

    print('True') if 'data/simple_demo.pdf' else print('False')
    print('True') if 'data/some.csv' else print('False')
    print('True') if 'data/test_with_files.xlsx' else print

# тут читаем csv файлы
with open('data/some.csv', newline='') as f:
    for row in csv.reader(f):
        print(f'\nРабота с CSV: {row} \n\nПроверка: ')

    print('True') if 'California' in row else print('False')
    print('True') if ['California', 'Sacramento', 'Los Angeles', '39538223'] == row else print('False')
    print('True') if len(row) == 4 else print('False')

# тут раболта с pdf
pdf_document = "data/simple_demo.pdf"
with open(pdf_document, "rb") as filehandle:
    # читает pdf file
    pdf = PdfFileReader(filehandle)
    page1 = pdf.getPage(0)
    text = page1.extractText()
    print(f'\nТекст из PDF: {text}\nПроверка pdf:')
    # тесты
    print(re.findall(r'^\w+', text, flags=re.IGNORECASE) == ['Welcome'])
    text_from = re.findall(r'\w+', text, flags=re.IGNORECASE)
    print('Welcome' in text_from)
    print('to' in text_from)
    print('Python' in text_from)
    print(len(text_from) == 3)

# тут читаем exel
book = load_workbook('data/test_with_files.xlsx')
sheet = book.active
ass = sheet.cell(row=3, column=3).value
print(f"\nЧитает определенную часть{ass}")# читаем exel
print(f"Строки и столбцы: {sheet.max_row}, {sheet.max_column}")
print(f"Проверка: {sheet.max_row==11}, {sheet.max_column==8}")
print(ass == 25000)
