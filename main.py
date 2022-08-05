from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
from view import *


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
janela.title("Agenda")
janela.geometry("1043x413")
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
app_nome = Label(frame_cima, text="Formulário de Consultas", anchor=NW, font="Ivy 13 bold",
                 bg=verde, fg=branco, relief=FLAT)
app_nome.place(x=10, y=20)


# Funções dos botões:
global tree


def inserir():
    nome = e_nome.get()
    email = e_email.get()
    telefone = e_telefone.get()
    estado = e_estado.get()
    comentario = e_comentario.get()
    dia = e_consulta.get()

    lista = [nome, email, telefone, dia, estado, comentario]

    if nome == '' or email == '' or telefone == '' or estado == '' or comentario == '' or dia == '':
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

    else:
        inserir_info(lista)
        messagebox.showinfo("Concluído", "Dados inseridos com sucesso!")
        e_nome.delete(0, 'end')
        e_email.delete(0, 'end')
        e_telefone.delete(0, 'end')
        e_estado.delete(0, 'end')
        e_comentario.delete(0, 'end')
        e_consulta.delete(0, 'end')

    for widget in frame_direita.winfo_children():
        widget.destroy

    mostrar()


def atualizarform():

    try:
        treev_dados = tree.focus()
        treev_dicinario = tree.item(treev_dados)
        tree_lista = treev_dicinario['values']
        valor_id = tree_lista[0]

        e_nome.delete(0, 'end')
        e_email.delete(0, 'end')
        e_telefone.delete(0, 'end')
        e_estado.delete(0, 'end')
        e_comentario.delete(0, 'end')
        e_consulta.delete(0, 'end')

        e_nome.insert(0, tree_lista[1])
        e_email.insert(0, tree_lista[2])
        e_telefone.insert(0, tree_lista[3])
        e_consulta.insert(0, tree_lista[4])
        e_estado.insert(0, tree_lista[5])
        e_comentario.insert(0, tree_lista[6])

        def update():
            nome = e_nome.get()
            email = e_email.get()
            telefone = e_telefone.get()
            estado = e_estado.get()
            comentario = e_comentario.get()
            dia = e_consulta.get()

            lista = [nome, email, telefone, dia, estado, comentario, valor_id]

            if nome == '' or email == '' or telefone == '' or estado == '' or comentario == '' or dia == '':
                messagebox.showerror(
                    "Erro", "Por favor, preencha todos os campos.")

            else:
                atualizar_info(lista)
                messagebox.showinfo(
                    "Concluído", "Dados atualizados com sucesso!")
                e_nome.delete(0, 'end')
                e_email.delete(0, 'end')
                e_telefone.delete(0, 'end')
                e_estado.delete(0, 'end')
                e_comentario.delete(0, 'end')
                e_consulta.delete(0, 'end')

            for widget in frame_direita.winfo_children():
                widget.destroy
                botao_confirmar.destroy()

        botao_confirmar = Button(frame_baixo, command=update, width=10, text="Confirmar",
                                 font="Ivy 10 bold", padx=0, bg=verde, fg=branco, relief=FLAT, overrelief=RAISED)
        botao_confirmar.place(x=110, y=280)

        mostrar()

    except IndexError:
        messagebox.showerror("Erro", "Selecione o contato a ser alterado")


def deletarform():
    try:
        treev_dados = tree.focus()
        treev_dicinario = tree.item(treev_dados)
        tree_lista = treev_dicinario['values']
        valor_id = [tree_lista[0]]

        deletar_info(valor_id)
        messagebox.showinfo("Concluído", "Contato deletado com sucesso.")

        for widget in frame_direita.winfo_children():
            widget.destroy()

        mostrar()

    except IndexError:
        messagebox.showerror("Erro", "Selecione o contato a ser alterado")


# Configurando frame baixo
l_nome = Label(frame_baixo, text="Nome*", anchor=NW, font="Ivy 10 bold",
               bg=branco, fg=preto, relief=FLAT)
l_nome.place(x=10, y=10)

e_nome = Entry(frame_baixo, width=45, justify=LEFT, relief=SOLID)
e_nome.place(x=13, y=30)


l_email = Label(frame_baixo, text="Email*", anchor=NW, font="Ivy 10 bold",
                bg=branco, fg=preto, relief=FLAT)
l_email.place(x=10, y=60)

e_email = Entry(frame_baixo, width=45, justify=LEFT, relief=SOLID)
e_email.place(x=13, y=80)


l_telefone = Label(frame_baixo, text="Telefone*", anchor=NW, font="Ivy 10 bold",
                   bg=branco, fg=preto, relief=FLAT)
l_telefone.place(x=10, y=110)

e_telefone = Entry(frame_baixo, width=45, justify=LEFT, relief=SOLID)
e_telefone.place(x=13, y=130)


l_consulta = Label(frame_baixo, text="Data da consulta*", anchor=NW, font="Ivy 10 bold",
                   bg=branco, fg=preto, relief=FLAT)
l_consulta.place(x=10, y=160)
e_consulta = DateEntry(frame_baixo, width=12,
                       background="darkblue", foreground='white', borderwidth=2, year=2022)
e_consulta.place(x=13, y=180)


l_estado = Label(frame_baixo, text="Urgência da consulta*", anchor=NW, font="Ivy 10 bold",
                 bg=branco, fg=preto, relief=FLAT)
l_estado.place(x=150, y=160)
e_estado = ttk.Combobox(frame_baixo, values=['Baixa', 'Moderada', 'Urgente'],
                        width=15)
e_estado.place(x=155, y=180)


l_comentario = Label(frame_baixo, text="Comentário*", anchor=NW, font="Ivy 10 bold",
                     bg=branco, fg=preto, relief=FLAT)
l_comentario.place(x=10, y=210)

e_comentario = Entry(frame_baixo, width=45, justify=LEFT, relief=SOLID)
e_comentario.place(x=13, y=230)


botao_inserir = Button(frame_baixo, command=inserir, width=10, text="Inserir",
                       font="Ivy 10 bold", padx=0, bg=azul, fg=branco, relief=FLAT, overrelief=RAISED)
botao_inserir.place(x=13, y=280)

botao_atualizar = Button(frame_baixo, command=atualizarform, width=10, text="Atualizar",
                         font="Ivy 10 bold", padx=0, bg=verde, fg=branco, relief=FLAT, overrelief=RAISED)
botao_atualizar.place(x=110, y=280)

botao_deletar = Button(frame_baixo, command=deletarform, width=10, text="Deletar",
                       font="Ivy 10 bold", padx=0, bg=vermelho, fg=branco, relief=FLAT, overrelief=RAISED)
botao_deletar.place(x=210, y=280)

# Lista no frame da direita


def mostrar():

    global tree

    lista = mostrar_info()

    tabela_head = ['ID', 'Nome',  'Email',
                   'Telefone', 'Data', 'Urgencia', 'Comentário']

    tree = ttk.Treeview(frame_direita, selectmode="extended",
                        columns=tabela_head, show="headings")

    vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

    hsb = ttk.Scrollbar(frame_direita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_direita.grid_rowconfigure(0, weight=12)

    hd = ["nw", "nw", "nw", "nw", "nw", "center", "center"]
    h = [30, 170, 140, 100, 70, 70, 130]
    n = 0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[n], anchor=hd[n])

        n += 1

    for item in lista:
        tree.insert('', 'end', values=item)


mostrar()

janela.mainloop()
