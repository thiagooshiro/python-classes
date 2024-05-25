
from auxiliar import adicionar_tarefas, ver_tarefas

lista_tarefas = []
def main():
    print('Bem vindo, à Lista de Tarefas1')
    print('1 - Adicionar tarefa')
    print('2 - Ver tarefas')
    print('3 - Sair')
    print('-'*10)

    num = int(input('Escolha uma opção'))
    if num == 1:
        adicionar_tarefas(lista_tarefas, main)
    elif num == 2:
        ver_tarefas(lista_tarefas, main)
categoria_urgencia = ['Alta', 'Media', 'Baixa']

lista_tarefas = [
    {'nome_tarefa': 'Estudar para o exame de matemática', 'categoria': 'estudo', 'urgencia': (1, 'Alta'), 'realizada': False},
    {'nome_tarefa': 'Preparar apresentação para reunião', 'categoria': 'erabalho', 'urgencia': (2, 'Média'), 'realizada': False},
    {'nome_tarefa': 'Ir ao supermercado', 'categoria': 'compras', 'urgencia': (3, 'Baixa'), 'realizada': False},
    {'nome_tarefa': 'Fazer exercícios físicos', 'categoria': 'saúde', 'urgencia': (1, 'Alta'), 'realizada': False},
    {'nome_tarefa': 'Ler o novo livro de ficção científica', 'categoria': 'lazer', 'urgencia': (2, 'Média'), 'realizada': False},
    {'nome_tarefa': 'Resolver pendências administrativas', 'categoria': 'trabalho', 'urgencia': (3, 'Baixa'), 'realizada': False},
    {'nome_tarefa': 'Estudar para prova de história', 'categoria': 'estudo', 'urgencia': (1, 'Alta'), 'realizada': False},
    {'nome_tarefa': 'Assistir aula online sobre programação', 'categoria': 'estudo', 'urgencia': (2, 'Média'), 'realizada': False},
    {'nome_tarefa': 'Fazer limpeza no apartamento', 'categoria': 'casa', 'urgencia': (3, 'Baixa'), 'realizada': False},
    {'nome_tarefa': 'Ligar para o serviço de manutenção do carro', 'categoria': 'casa', 'urgencia': (1, 'Alta'), 'realizada': False}
]




def definir_urgencia():
    print('Qual a urgência da tarefa? ')
    print('1 - Alta', '2 - Média', '3 - Baixa', sep='\n')
    urgencia = input('Digite aqui a urgência da tarefa: ')
    result = ''
    while urgencia not in '123':
        print('-'*10)
        print('Opção inválida, tente novamente')
        print('-'*10)       
        print('1 - Alta', '2 - Média', '3 - Baixa', sep='\n')
        urgencia = input('Digite aqui a urgência da tarefa: ')
    else:
        result = int(urgencia)
        print(result)
        return result
        

    

def exibir_realizada(realizada):
    if realizada:
        return 'Realizada'
    else:
        return 'Não realizada'


def adicionar_tarefas():
    nome_tarefa = input('Qual a tarefa a ser realizada?')
    categoria = input('Qual categoria da tarefa? ').lower()
    urgencia = definir_urgencia()

    realizada = False
    tarefa = {
        'nome_tarefa': nome_tarefa,
        'categoria': categoria,
        'urgencia': (urgencia, categoria_urgencia[urgencia-1]),
        'realizada': realizada
    }
    lista_tarefas.append(tarefa)
    print('Tarefa adicionada com sucesso!')
    print('-'*10)
    continuar = input('Deseja continuar?S/N')
    if continuar.lower() == 's':
        main()


def ver_geral(lista_tarefas):
    for tarefa in lista_tarefas:
        print('Tarefa: ', tarefa['nome_tarefa'])
        print('Categoria: ', tarefa['categoria'])
        print('Urgencia: ', tarefa['urgencia'][1])
        print('Realizada: ', exibir_realizada(tarefa['realizada']))
        print('-'*10)


def ver_urgencia():
    result = sorted(lista_tarefas, key= lambda x :x['urgencia'][0])
    ver_geral(result)
    


def filtrar_categoria():
    print('Digite a categoria pela qual deseja filtrar')
    filtro = input('Palavra a ser filtrada')
    lista_filtrada = [i for i in lista_tarefas if i['categoria'] in filtro]
    print(lista_filtrada)
    ver_geral(lista_filtrada)



def ver_tarefas():
    print('Escolha uma das opções:')
    print('1 - Ver todas as tarefas')
    print('2 - Ver tarefas classificadas por urgencia')
    print('3 - Filtrar tarefas por categoria')
    escolha = input('Digite um número para escolher: ')
    
    if escolha == '1':
        ver_geral(lista_tarefas)
    if escolha == '2':
        ver_urgencia()
    if escolha == '3':
        filtrar_categoria()
    main()
    


def main():
    print('Bem vindo, à Lista de Tarefas!')
    print('1 - Adicionar tarefa')
    print('2 - Ver tarefas')
    print('3 - Concluir tarefa')
    print('4 - Sair')
    print('-'*10)


    num = input('Escolha uma opção: ')

    if num == '1':
        adicionar_tarefas()
    elif num == '2':
        ver_tarefas()
    elif num  == '3':
        pass
    elif num == '4':
        pass






main()