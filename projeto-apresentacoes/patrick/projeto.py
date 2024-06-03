controle = True
tarefas = []
while controle:
    def escolha():
        print("1- adicionar nova tarefa")
        print("2-ver todas as tarefas")
        print("3-marcar tarefa como concluídas")
        print("4-Classificar tarefas -> : Categoria e urgencia")
        print("6-Sair")
    escolha()
    escolha = int(input("O que voce deseja:"))
    if escolha == 1:
        def adicionar_tarefa():
            nome_tarefa = str(input("informe o nome da tarefa: "))
            descriçao= str(input("Informe a descricao: "))
            prioridade = str(input("Informe a prioridade: "))
            categoria = str(input("Informe a categoria: "))
            realizada = False
            dicionario = {
                "nome": nome_tarefa,
                "descriçao": descriçao,
                "prioridade": prioridade,
                "categoria": categoria,
                "concluida": realizada
            }
            tarefas.append(dicionario)
        adicionar_tarefa()
    elif escolha == 2:
        def visualizar():
            print(tarefas)
        visualizar()
    elif escolha == 3:
        def concluida():
            nome = input("informe o nome da tarefa que queira concluir: ")
            for item in tarefas:
                if item["nome"] == nome:
                    if item["concluida"] == False:
                        item["concluida"] = True
                    else:
                        print("Tarefa concluida")
        concluida()
    # elif escolha == 4:
    #     def classificar_tarefas(tarefas):
   
    #         tarefas_ordenadas = sorted(tarefas, key=lambda tarefa: (tarefa['categoria'], tarefa['prioridade']))
      
    #         visualizar_tarefas(tarefas_ordenadas)
    #         classificar_tarefas()
