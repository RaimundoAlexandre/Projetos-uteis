# github RaimundoAlexandre
from tkinter import END, messagebox

import customtkinter as ctk

app = ctk.CTk()
app.geometry('240x300+800+200')
app.title('Calculadora')
app.resizable(width=False, height=False)
font1 = ('Arial', 20, 'bold')

# caixa de texto, aqui aparece o resultado
box_texto = ctk.CTkEntry(app, font=font1, placeholder_text='', width=200, height=40)
box_texto.place(x=20, y=10)


# Funções
def bt_click(num):
    box_texto.insert(END, num)


def limpar():
    box_texto.delete(0, END)


def calcular():
    try:
        valor = box_texto.get().replace('x', '*')
        resultado = eval(valor)
        limpar()
        box_texto.insert(0, resultado)
    except NameError:
        messagebox.showerror('ERRO', 'Valor invalido')
    except ZeroDivisionError:
        messagebox.showerror('ERRO', 'Nao pode dividir por 0')
    except SyntaxError:
        messagebox.showerror('ERRO', 'Digite um valor para poder calcular')


# botões de calculo

bt_c = ctk.CTkButton(app, width=50, height=30, text='C', font=font1, command=limpar)
bt_c.place(relx=0.53, rely=0.36)
bt_soma = ctk.CTkButton(app, width=50, height=30, text='+', font=font1, command=lambda: bt_click('+'))
bt_soma.place(relx=0.75, rely=0.36)
bt_sub = ctk.CTkButton(app, width=50, height=30, text='-', font=font1, command=lambda: bt_click('-'))
bt_sub.place(relx=0.75, rely=0.48)
bt_div = ctk.CTkButton(app, width=50, height=30, text='/', font=font1, command=lambda: bt_click('/'))
bt_div.place(relx=0.75, rely=0.59)
bt_mult = ctk.CTkButton(app, width=50, height=30, text='x', font=font1, command=lambda: bt_click('x'))
bt_mult.place(relx=0.75, rely=0.7)
bt_resu = ctk.CTkButton(app, width=50, height=30, text='=', font=font1, command=calcular)
bt_resu.place(relx=0.75, rely=0.81)
# botões numerados de 0 a 9

bt1 = ctk.CTkButton(app, width=50, height=30, text='1', font=font1, command=lambda: bt_click('1'))
bt1.place(relx=0.07, rely=0.7)
bt2 = ctk.CTkButton(app, width=50, height=30, text='2', font=font1, command=lambda: bt_click('2'))
bt2.place(relx=0.30, rely=0.7)
bt3 = ctk.CTkButton(app, width=50, height=30, text='3', font=font1, command=lambda: bt_click('3'))
bt3.place(relx=0.53, rely=0.7)
bt4 = ctk.CTkButton(app, width=50, height=30, text='4', font=font1, command=lambda: bt_click('4'))
bt4.place(relx=0.07, rely=0.59)
bt5 = ctk.CTkButton(app, width=50, height=30, text='5', font=font1, command=lambda: bt_click('5'))
bt5.place(relx=0.30, rely=0.59)
bt6 = ctk.CTkButton(app, width=50, height=30, text='6', font=font1, command=lambda: bt_click('6'))
bt6.place(relx=0.53, rely=0.59)
bt7 = ctk.CTkButton(app, width=50, height=30, text='7', font=font1, command=lambda: bt_click('7'))
bt7.place(relx=0.07, rely=0.48)
bt8 = ctk.CTkButton(app, width=50, height=30, text='8', font=font1, command=lambda: bt_click('8'))
bt8.place(relx=0.30, rely=0.48)
bt9 = ctk.CTkButton(app, width=50, height=30, text='9', font=font1, command=lambda: bt_click('9'))
bt9.place(relx=0.53, rely=0.48)
bt0 = ctk.CTkButton(app, width=50, height=30, text='0', font=font1, command=lambda: bt_click('0'))
bt0.place(relx=0.30, rely=0.81)

app.mainloop()
