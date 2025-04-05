def adicionar_tarefas(lista_tarefas, main):
    nome_tarefa = input('Qual a tarefa a ser realizada?')
    categoria = input('Qual categoria da tarefa')
    urgencia = input('Qual urgencia')
    realizada = False
    tarefa = {
        'nome da tarefa': nome_tarefa,
        'categoria': categoria,
        'urgencia': urgencia,
        'realizada': realizada
    }
    lista_tarefas.append(tarefa)
    main()


def ver_tarefas(lista_tarefas):
    for tarefa in lista_tarefas:
        print('-'*10)
        print('Nome da Tarefa: ', tarefa['nome da tarefa'])
        print('Categoria: ', tarefa['categoria'])
        print('Urgencia: ', tarefa['urgencia'])
        print('Realizada: ', tarefa['realizada'])
        print('-'*10)
    main()