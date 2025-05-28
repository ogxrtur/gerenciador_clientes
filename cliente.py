from db import conectar

def adicionar_cliente(nome, email):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", (nome, email))

def listar_clientes():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clientes")
        return cursor.fetchall()

def atualizar_cliente(id, novo_nome, novo_email):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE clientes SET nome = ?, email = ? WHERE id = ?", (novo_nome, novo_email, id))       
        conn.commit()

def deletar_cliente(id):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM clientes WHERE id = ?", (id,))
        conn.commit()