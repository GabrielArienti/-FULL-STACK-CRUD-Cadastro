import sqlite3 as lite

# CRUD
con = lite.connect('dados.db')

# função inserir (criar)


def inserir_info(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO formulario (nome, email, telefone, dia_em, estado, comentario) VALUES(?, ?, ?, ?, ?, ?)"
        cur.execute(query, i)


# Acessar info

def mostrar_info():
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM formulario"
        cur.execute(query)
        info = cur.fetchall()

        for i in info:
            lista.append(i)
    return lista


# Atualizar informações:

def atualizar_info(i):
    with con:
        cur = con.cursor()
        query = "UPDATE formulario SET nome=?, email=?, telefone=?, dia_em=?, estado=?, comentario=? WHERE id=?"
        cur.execute(query, i)


# Deletar informações
def deletar_info(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM formulario WHERE id=?"
        cur.execute(query, i)
