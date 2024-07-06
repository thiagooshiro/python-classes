# Lista para armazenar os cadastros dos membros
cadastros = []

def adicionar_membro(id, nome, idade, email):
    for membro in cadastros:
        if membro['id'] == id:
            print("Membro com este ID já existe.")
            return
    novo_membro = {
        'id': id,
        'nome': nome,
        'idade': idade,
        'email': email
    }
    cadastros.append(novo_membro)
    print(f"Membro {nome} adicionado com sucesso!")

def visualizar_membros():
    if not cadastros:
        print("Nenhum membro cadastrado.")
    else:
        for membro in cadastros:
            print(f"ID: {membro['id']}, Nome: {membro['nome']}, Idade: {membro['idade']}, Email: {membro['email']}")

def atualizar_membro(id, nome=None, idade=None, email=None):
    for membro in cadastros:
        if membro['id'] == id:
            if nome:
                membro['nome'] = nome
            if idade:
                membro['idade'] = idade
            if email:
                membro['email'] = email
            print(f"Membro {id} atualizado com sucesso!")
            return
    print("Membro não encontrado.")

def remover_membro(id):
    for membro in cadastros:
        if membro['id'] == id:
            cadastros.remove(membro)
            print(f"Membro {id} removido com sucesso!")
            return
    print("Membro não encontrado.")

def stalkear_membros(nome):
    for membro in cadastros:
        if membro['nome'] == nome:
            print(f'Membro encontrado: {membro['nome']}, {membro['email']}')
            return
    print('Membro não encontrado')

# Exemplo de uso das funções
adicionar_membro(1, "Ana", 25, "ana@example.com")
adicionar_membro(2, "Bruno", 30, "bruno@example.com")
visualizar_membros()

atualizar_membro(1, idade=26)
visualizar_membros()

stalkear_membros('Ana')
