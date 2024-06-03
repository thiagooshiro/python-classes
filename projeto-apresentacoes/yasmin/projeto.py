# Definição de uma lista de tarefas
tarefas = []

# Função para adicionar uma nova tarefa
def adicionar_tarefa(nome, descricao, prioridade, categoria):
    tarefa = {
        'nome': nome,
        'descricao': descricao,
        'prioridade': prioridade,
        'categoria': categoria,
        'concluida': False  # Adicionamos um campo para indicar se a tarefa está concluída ou não
    }
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

# Função para listar todas as tarefas
def listar_tarefas():
    if not tarefas:
        print("Não há tarefas cadastradas.")
    else:
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"Tarefa {i}:")
            print(f"Nome: {tarefa['nome']}")
            print(f"Descrição: {tarefa['descricao']}")
            print(f"Prioridade: {tarefa['prioridade']}")
            print(f"Categoria: {tarefa['categoria']}")
            print(f"Concluída: {'Sim' if tarefa['concluida'] else 'Não'}")
            print()

# Função para marcar uma tarefa como concluída
def marcar_tarefa_concluida(numero_tarefa):
    if 1 <= numero_tarefa <= len(tarefas):
        tarefas[numero_tarefa - 1]['concluida'] = True
        print("Tarefa marcada como concluída!")
    else:
        print("Número de tarefa inválido.")

# Função para exibir tarefas por prioridade
def exibir_tarefas_por_prioridade(prioridade):
    print(f"Tarefas com prioridade '{prioridade}':")
    for tarefa in tarefas:
        if tarefa['prioridade'] == prioridade:
            print(f"Nome: {tarefa['nome']}")

# Função para exibir tarefas por categoria
def exibir_tarefas_por_categoria(categoria):
    print(f"Tarefas na categoria '{categoria}':")
    for tarefa in tarefas:
        if tarefa['categoria'] == categoria:
            print(f"Nome: {tarefa['nome']}")

# Função para listar tarefas concluídas
def listar_tarefas_concluidas():
    print("Tarefas concluídas:")
    for tarefa in tarefas:
        if tarefa['concluida']:
            print(f"Nome: {tarefa['nome']}")
            print(f"Descrição: {tarefa['descricao']}")
            print()

# Função para remover uma tarefa
def remover_tarefa(numero_tarefa):
    if 1 <= numero_tarefa <= len(tarefas):
        del tarefas[numero_tarefa - 1]
        print("Tarefa removida com sucesso!")
    else:
        print("Número de tarefa inválido.")

# Função para exibir o menu de comandos
def exibir_menu():
    print("====== Menu de Tarefas ======")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Exibir tarefas por prioridade")
    print("5. Exibir tarefas por categoria")
    print("6. Listar tarefas concluídas")
    print("7. Remover tarefa")
    print("8. Sair")
    print("=============================")

# Loop principal do programa
while True:
    exibir_menu()
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        nome = input("Nome da tarefa: ")
        descricao = input("Descrição da tarefa: ")
        prioridade = input("Prioridade da tarefa: ")
        categoria = input("Categoria da tarefa: ")
        adicionar_tarefa(nome, descricao, prioridade, categoria)
    elif escolha == '2':
        listar_tarefas()
    elif escolha == '3':
        numero_tarefa = int(input("Número da tarefa a ser marcada como concluída: "))
        marcar_tarefa_concluida(numero_tarefa)
    elif escolha == '4':
        prioridade = input("Prioridade a ser filtrada: ")
        exibir_tarefas_por_prioridade(prioridade)
    elif escolha == '5':
        categoria = input("Categoria a ser filtrada: ")
        exibir_tarefas_por_categoria(categoria)
    elif escolha == '6':
        listar_tarefas_concluidas()
    elif escolha == '7':
        numero_tarefa = int(input("Número da tarefa a ser removida: "))
        remover_tarefa(numero_tarefa)
    elif escolha == '8':
        print("Vai lá preguiçoso!")
        break
    else:
        print("Isso não existe. Coloque algo que exista seu burro!")
