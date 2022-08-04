from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from pyparsing import col


# Cores
branco = "#fcfcfc"
branco_claro = "#f2f2f2"
preto = "#030303"
preto_cinza = "#1f1d1d"
azul = "#407ee3"
amarelo = "#edfa00"
laranja = "#fa9200"
vermelho = "#8c0601"
verde = "#32a852"
ganho = "#6dd695"

# Janela

janela = Tk()
janela.title("Formulário de Contatos")
janela.geometry("1043x453")
janela.configure(bg=branco_claro)
janela.resizable(width=FALSE, height=FALSE)

# Frames

frame_cima = Frame(janela, width=310, height=50, bg=verde, relief=FLAT)
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=400, bg=branco, relief=FLAT)
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_direita = Frame(janela, width=588, height=400, bg=branco, relief=FLAT)
frame_direita.grid(row=0, column=1, rowspan=2, pady=0, padx=1, sticky=NSEW)

# Configurando frame cima
app_nome = Label(frame_cima, text="Formulário de Contatos", anchor=NW, font="Ivy 13 bold",
                 bg=verde, fg=branco, relief=FLAT)
app_nome.place(x=10, y=20)


janela.mainloop()
