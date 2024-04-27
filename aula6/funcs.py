
lista_tarefas = []
def main():
    print('Bem vindo, à Lista de Tarefas1')
    print('1 - Adicionar tarefa')
    print('2 - Ver tarefas')
    print('3 - Sair')
    print('-'*10)

    num = int(input('Escolha uma opção'))
    if num == 1:
        adicionar_tarefas()
    elif num == 2:
        ver_tarefas()
    else:
        pass


def adicionar_tarefas():
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

def ver_tarefas():
    for tarefa in lista_tarefas:
        print('-'*10)
        print('Nome da Tarefa: ', tarefa['nome da tarefa'])
        print('Categoria: ', tarefa['categoria'])
        print('Urgencia: ', tarefa['urgencia'])
        print('Realizada: ', tarefa['realizada'])
        print('-'*10)
    main()


main()