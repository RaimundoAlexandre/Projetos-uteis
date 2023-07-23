# github RaimundoAlexandre
from tkinter import *

janela = Tk()
janela.geometry("260x300+200+200")
janela.title("Calculadora")
janela.resizable(width=False, height=False)

def bt_soma():
    if str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric():
        n1 = int(ed1.get())
        n2 = int(ed2.get())
        lb["text"] = n1 + n2
    else:
        lb["text"] = "Valor invalido"


def bt_mult():
    if str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric():
        n1 = int(ed1.get())
        n2 = int(ed2.get())
        lb["text"] = n1 * n2
    else:
        lb["text"] = "Valor invalido"


def bt_div():
    if str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric():
        n1 = int(ed1.get())
        n2 = int(ed2.get())
        lb["text"] = n1 / n2
    else:
        lb["text"] = "Valor invalido"


def sub_tracao():
    if str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric():
        n1 = int(ed1.get())
        n2 = int(ed2.get())
        lb["text"] = n1 - n2
    else:
        lb["text"] = "Valor invalido"

# caixa1
ed1 = Entry(janela)
ed1.place(x=50, y=30, width=50)
# caixa2
ed2 = Entry(janela)
ed2.place(x=105, y=30, width=50)
# texto
lb = Label(janela, width=20, text="===" * 5)
lb.place(x=40, y=50)
# botões
btSoma = Button(janela, width=10, text="+", command=bt_soma)
btSoma.place(x=180, y=100)
btMult = Button(janela, width=10, text="x", command=bt_mult)
btMult.place(x=180, y=130)
btDiv = Button(janela, width=10, text="/", command=bt_div)
btDiv.place(x=180, y=160)
btSub = Button(janela, width=10, text="-", command=sub_tracao)
btSub.place(x=180, y=190)

janela.mainloop()
