from pdf2image import convert_from_path
import pytesseract
import pandas as pd


from parser_is import ISParser
from parser_bs import BSParser

POPPLER_PATH = r'C:\poppler-22.12.0\Library\bin'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def extract_fs(file_path):
    # extracting text from pdf files

    img = convert_from_path(file_path, poppler_path=POPPLER_PATH)

    searchstring1 = "Statement of Operations"
    searchstring2 = "Interest revenue"
    searchstring3 = "Statement of Financial Position"
    searchstring4 = "Accounts payable"
    fs = ''

    for i in img:
        text = pytesseract.image_to_string(i, lang='eng')
        if (searchstring1 in text and searchstring2 in text) or (searchstring3 in text and searchstring4 in text):
            fs = fs + '' + text

    # step 2: extract fields from text

    data1 = ISParser(fs).parse()
    data2 = BSParser(fs).parse()
    extracted_data = data1 | data2

    #step 3: write to excel

    extracted_data = pd.DataFrame(extracted_data)

    file_path = "../uploads/data.xlsx"
    extracted_data.to_excel(file_path, index=False)

    return extracted_data


if __name__ == '__main__':

    data = extract_fs(r'..\uploads\merged_reports.pdf')
    print(data)



