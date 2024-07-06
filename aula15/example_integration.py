import mysql.connector

# Conectando ao banco de dados
conexao = mysql.connector.connect(
    host="localhost",
    user="seu_usuario",
    password="sua_senha",
    database="nome_do_banco_de_dados"
)

cursor = conexao.cursor()


comando_sql = """
CREATE TABLE Alunos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    idade INT,
    curso VARCHAR(100)
);
"""
cursor.execute(comando_sql)
conexao.commit()
