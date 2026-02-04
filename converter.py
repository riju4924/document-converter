from docx2pdf import convert
from pdf2docx import Converter


def word_to_pdf(input_path, output_path):
    convert(input_path, output_path)


def pdf_to_word(input_path, output_path):
    cv = Converter(input_path)
    cv.convert(output_path)
    cv.close()
