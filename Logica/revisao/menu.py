senhas = ['12A', '14B', '42']

validado = False
print('Bem vindo à lista de tarefas')
digitado = input('Digite sua senha de acesso: ')
tarefas = []
while True:
   
    if digitado in senhas:
        validado = True      
    else:
        digitado = input('Senha incorreta, digite novamente')
        continue

    print('Escolha uma das ações: ')
    print('1 - Adicionar Tarefa')
    print('2 - Listar tarefas')
    print('3 - Concluir tarefa')
    print('4 - Sair')
    opcao = input('Digite sua opção: ')

    if opcao == '1':
        tarefa = input('Digite a tarefa a ser adicionada: ')
        tarefas.append(tarefa)
        continuar = input('Deseja continuar?s/n: ')
        if continuar[0].lower() != 's':
            break
    if opcao == '2':
        n = 1
        print('-----------------------')
        print('Tarefas:')
        for tarefa in tarefas:
            print(f'{n} - {tarefa}')
            n += 1
        print('----------------------')
        continuar = input('Deseja continuar?s/n: ')
        if continuar[0].lower() != 's':
            break
    if opcao == '3':
        n = 1
        for tarefa in tarefas:
            print(f'{n} - {tarefa}')
            n += 1
        concluir = int(input('Digite o número da tarefa que deseja marcar como concluída: '))
        tarefas.remove(tarefas[concluir - 1])
        print('Tarefa removida com sucesso')
        continuar = input('Deseja continuar?s/n: ')
        if continuar[0].lower() != 's':
            break

    if opcao == '4':
        break