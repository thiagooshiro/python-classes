from db import get_connection

def criar_escola(nome, tipo_escola, telefone=None, email=None, endereco=None, cidade=None, estado=None, cep=None):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO Escolas (nome, tipo_escola, telefone, email, endereco, cidade, estado, cep)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (nome, tipo_escola, telefone, email, endereco, cidade, estado, cep))

    conn.commit()
    conn.close()

def listar_escolas():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Escolas')
    escolas = cursor.fetchall()

    conn.close()
    return escolas
