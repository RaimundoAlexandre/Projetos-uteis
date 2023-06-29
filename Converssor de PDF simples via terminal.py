from pdf2docx import Converter

def convert_pdf_to_docx(pdf_file, docx_file):
    cv = Converter(pdf_file)
    cv.convert(docx_file, start=0, end=None)
    cv.close()

pdf_file = input("Digite o nome do 'arquivo.pdf': ")
docx_file = "Novo_arquivo.docx"

convert_pdf_to_docx(pdf_file, docx_file)
