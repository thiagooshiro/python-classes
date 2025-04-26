import sqlite3
import streamlit as st

# Inicializa banco
def iniciar_banco():
    conexao = sqlite3.connect("banco_de_dados.db")
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL
        );
    ''')
    conexao.commit()
    return conexao, cursor

# Função para cadastrar usuário
def cadastrar_usuario(nome, email):
    conexao, cursor = iniciar_banco()
    cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
    conexao.commit()

# Função para listar usuários
def listar_usuarios():
    conexao, cursor = iniciar_banco()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    return usuarios

# Função para buscar usuário por ID
def buscar_usuario_por_id(id):
    conexao, cursor = iniciar_banco()
    cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id,))
    usuario = cursor.fetchone()
    return usuario

# Função para atualizar usuário
def atualizar_usuario(id, nome, email):
    conexao, cursor = iniciar_banco()
    cursor.execute("UPDATE usuarios SET nome = ?, email = ? WHERE id = ?", (nome, email, id))
    conexao.commit()

# Função para deletar usuário
def deletar_usuario(id):
    conexao, cursor = iniciar_banco()
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    conexao.commit()

# Função para exibir a interface do Streamlit
def main():
    st.title("CRUD com Streamlit + SQLite")

    # Formulário de entrada de dados
    nome = st.text_input("Nome")
    email = st.text_input("Email")
    id_buscar = st.text_input("ID (para buscar, atualizar ou deletar)")

    # Ações do CRUD
    if st.button("Cadastrar Usuário"):
        if nome and email:
            cadastrar_usuario(nome, email)
            st.success("Usuário cadastrado com sucesso!")
        else:
            st.warning("Por favor, preencha nome e email.")

    # Listar usuários
    if st.button("Listar Usuários"):
        usuarios = listar_usuarios()
        if usuarios:
            st.write("### Usuários Cadastrados:")
            for u in usuarios:
                st.write(f"ID: {u[0]} | Nome: {u[1]} | Email: {u[2]}")
        else:
            st.warning("Nenhum usuário cadastrado.")

    # Buscar por ID
    if st.button("Buscar Usuário por ID"):
        if id_buscar:
            usuario = buscar_usuario_por_id(id_buscar)
            if usuario:
                st.write(f"ID: {usuario[0]} | Nome: {usuario[1]} | Email: {usuario[2]}")
            else:
                st.warning("Usuário não encontrado.")
        else:
            st.warning("Por favor, digite um ID.")

    # Atualizar dados do usuário
    if st.button("Atualizar Usuário"):
        if id_buscar and nome and email:
            atualizar_usuario(id_buscar, nome, email)
            st.success("Usuário atualizado com sucesso!")
        else:
            st.warning("Preencha todos os campos para atualizar.")

    # Deletar usuário
    if st.button("Deletar Usuário"):
        if id_buscar:
            deletar_usuario(id_buscar)
            st.success("Usuário deletado com sucesso!")
        else:
            st.warning("Por favor, digite um ID para deletar.")

if __name__ == "__main__":
    main()