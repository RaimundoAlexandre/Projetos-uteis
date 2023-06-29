#guithub: RaimundoAlexandre
import tkinter as tk
from tkinter import filedialog
from pdf2docx import Converter

class PDFtoDOCXConverter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Conversor de PDF para DOCX")
        self.root.geometry("400x200")  # Define um tamanho fixo para a janela

        # Cria os elementos da interface
        self.label = tk.Label(self.root, text="Nome do arquivo PDF:")
        self.label.pack(pady=10)  # Adiciona um espaçamento entre o rótulo e o campo de entrada

        self.entry = tk.Entry(self.root, width=40)  # Aumenta a largura do campo de entrada
        self.entry.pack()

        self.button = tk.Button(self.root, text="Converter", command=self.convert_pdf_to_docx)
        self.button.pack(pady=10)  # Adiciona um espaçamento entre o campo de entrada e o botão

        self.result_label = tk.Label(self.root, text="", wraplength=380)  # Define uma largura máxima para o rótulo de resultado
        self.result_label.pack()

    def convert_pdf_to_docx(self):
        # Obtém o nome do arquivo PDF inserido pelo usuário
        pdf_file = self.entry.get()

        if pdf_file.endswith(".pdf"):
            # Cria o nome do arquivo DOCX de saída substituindo a extensão
            docx_file = pdf_file.replace('.pdf', '.docx')

            # Cria uma instância do conversor de PDF para DOCX
            cv = Converter(pdf_file)
            # Realiza a conversão do PDF para DOCX, especificando o arquivo de saída
            cv.convert(docx_file, start=0, end=None)
            # Fecha o conversor após a conversão
            cv.close()

            # Exibe uma mensagem de sucesso
            self.result_label.config(text=f"Conversão concluída. Arquivo DOCX salvo como: {docx_file}")
        else:
            # Exibe uma mensagem de erro caso a extensão do arquivo seja inválida
            self.result_label.config(text="Extensão de arquivo inválida. Insira um arquivo PDF.")

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    converter = PDFtoDOCXConverter()
    converter.run()
