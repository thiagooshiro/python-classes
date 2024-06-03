tarefas = [{"nome" : "Dentista", "descrição": "Dentista marcado as 10 horas", "prioridade" : 10, "categoria" : "Saúde", "status_conclusão" : False },
           {"nome" : "Comprar velas", "descrição": "Minhas velas acabaram, preciso comprar novas", "prioridade" : 3, "categoria" : "Compras", "status_conclusão" : True },
           {"nome" : "Encontro", "descrição": "Encontro marcado com meu namorado amanhã (27/04/2024) as 21 horas", "prioridade" : 8, "categoria" : "Hobbies", "status_conclusão" : False }]


def menu ():
    escolha = int(input(""" Bem vindo a sua lista de tarefas !!
    O que você deseja ?
    1 - Adicionar tarefa
    2 - Visualizar tarefas 
    3 - Marcar uma tarefa como concluída
    4 - Exibir tarefas por prioridade ou categoria
    5 - Remover uma tarefa
    6 - sair
    Digite o número referente a seu desejo:"""))
    if escolha == 1:
        adicionar_tarefa()
    elif escolha == 2:
        visualizar_tarefas ()
    elif escolha == 3:
        marcar_concluido ()
    elif escolha == 4:
        exibir_prioridade_categoria ()
    elif escolha == 5:
        remover_tarefa()
    elif escolha == 6:
        print("Muito obrigado, até a próxima!!")
    else:
        print("Número inválido!")
        menu()

def adicionar_tarefa ():
    print("Você deseja adicionar uma tarefa!")
    nome = input("Digite o nome da sua tarefa:")
    descrição = input("Digite a descrição da sua tarefa:")
    prioridade = int((input("Digite o número de prioridade da sua tarefa:")))
    categoria = input("Digite a categoria da sua tarefa:")
    status_tarefa = False
    nova_tarefa = {"nome" : nome, "descrição": descrição, "prioridade" : prioridade, "categoria" : categoria , "status_conclusão" : status_tarefa}
    tarefas.append(nova_tarefa)
    print("Nova tarefa adicionada!")
    menu()
        
def visualizar_tarefas ():
    i = 1
    print("Você deseja visualizar suas tarefas, aqui está:")
    for tarefa in tarefas: 
        texto = ""
        if tarefa["status_conclusão"] == False:
            texto = "Tarefa não realizada"
        else :
            texto = "Tarefa realizada"

        print(f"TAREFA {i}:")
        print("Nome da tarefa:" , tarefa["nome"])
        print("Descrição da tarefa:", tarefa["descrição"])
        print("Prioridade da tarefa:", tarefa["prioridade"])
        print("Categoria:", tarefa ["categoria"])
        print("Status da tarefa:", texto)
        i += 1
    menu ()
   
def marcar_concluido ():
    print("Você deseja marcar uma tarefa como conluída!")  
    tarefa_concluir = input("Digite o nome da tarefa que você deseja concluir:").lower()
    tarefa_encontrada = False
    for tarefa in tarefas:
        if tarefa["nome"].lower()  == tarefa_concluir:
            tarefa["status_conclusão"] = True
            print("Tarefa marcada como concluída!")
            tarefa_encontrada = True
    if not tarefa_encontrada:
        print("Tarefa não encontrada!")
    menu ()

def exibir_prioridade_categoria ():
    exibir_tarefa = int(input("""Você deseja exibir suas tarefas:
                              1 - Por prioridade
                              2 - Por categoria
                              Digite o número referente ao seu desejo:"""))
    if exibir_tarefa == 1:
        print("Exibir por prioridade, aqui está:")
        tarefas_ordenadas = sorted(tarefas, key=lambda x: x["prioridade"], reverse=True)
        i = 1
        for tarefa in tarefas_ordenadas:
            print(f"TAREFA {i}")
            print("Nome da tarefa:", tarefa["nome"]) 
            print("Prioridade: ", tarefa["prioridade"])
            print("Status de conclusão:", "Tarefa realizada!" if tarefa["status_conclusão"] == True else "Tarefa não realizada!")
            i += 1
    elif exibir_tarefa == 2:
        print("Você deseja exibir por categoria!")
        i = 1
        categoria_encontrada = False
        categoria = input("Digite a categoria que você deseja visualizar:").lower()
        for tarefa in tarefas:
            if tarefa["categoria"].lower() == categoria:
                print(f"TAREFA {i}")
                print("Nome da tarefa:", tarefa["nome"]) 
                print("Categoria: ", tarefa["categoria"])
                print("Status de conclusão:", "Tarefa realizada!" if tarefa["status_conclusão"] == True else "Tarefa não realizada!") 
                i += 1
                categoria_encontrada = True
        if not categoria_encontrada:
            print("Categoria não encontrada!")
    menu()

def remover_tarefa():
    print("Você deseja remover uma tarefa!!")
    tarefa_encontrada = False
    tarefa_remover = input("Digite o nome da tarefa que você deseja remover:").lower()
    for tarefa in tarefas:
        if tarefa["nome"].lower() == tarefa_remover:
            tarefas.remove(tarefa)
            print("Tarefa removida com sucesso!")
            tarefa_encontrada = True
    if not tarefa_encontrada:
        print("Essa tarefa não existe")
    menu()
menu()