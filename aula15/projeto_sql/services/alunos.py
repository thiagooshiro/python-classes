from db import get_connection

def criar_aluno(nome, data_nascimento, id_escola=None, telefone=None, email=None, endereco=None, cidade=None, estado=None, cep=None):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO Alunos (nome, data_nascimento, id_escola, telefone, email, endereco, cidade, estado, cep)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (nome, data_nascimento, id_escola, telefone, email, endereco, cidade, estado, cep))

    conn.commit()
    conn.close()

def listar_alunos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT Alunos.id, Alunos.nome, Alunos.data_nascimento, Escolas.nome AS nome_escola
        FROM Alunos
        LEFT JOIN Escolas ON Alunos.id_escola = Escolas.id
    ''')

    alunos = cursor.fetchall()
    conn.close()
    return alunos
