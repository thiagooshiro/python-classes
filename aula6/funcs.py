
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
    else:
        pass




main()