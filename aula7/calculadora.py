from operacoes import soma, multiplicacao, divisao, subtracao


def menu():
    print('Bem vindo a calculadora')
    print('Qual operação deseja executar?')
    print('1 - Soma', '2 - Subtração', '3 - Multilpicação', '4 - Divisão', '5 - Sair', sep='\n')
    oper = input('Escolha a operação: ')

    

    if oper == '5':
        return print('Tenha um bom dia!')
    
    if oper not in '12345' or oper == '':
        print('Operação inválida, tente novamente')
        return menu()

    try:
        n1 = float(input('Digite o primeiro valor'))
        n2 = float(input('Digite o segundo valor'))

        if oper == '1':
             print(soma(n1, n2))
        elif oper == '2':
            print(subtracao(n1, n2))
        elif oper == '3':
            print(multiplicacao(n1, n2))
        elif oper == '4':
            print(divisao(n1, n2, menu))

        continuar = input('Deseja continuar?S/N').lower()
        
        if continuar == 'sim' or continuar == 's':
            menu()
        else:
            print('Finalizando execução...')
            print('Tenha um bom dia!')
    
    except(ValueError):
        print('Digite apenas valores númericos, tente novamente')
        input('Pressione "Enter" para continuar')
        return menu()

   


menu()




def menu():
    print('Bem vindo a calculadora')
    print('Qual operação deseja executar?')
    print('1 - Soma', '2 - Subtração', '3 - Multilpicação', '4 - Divisão', '5 - Sair', sep='\n')
    oper = input('Escolha a operação: ')

    if oper == '1':
        # Chamar função pra somar
        pass #pass é só pra não quebrar o código, remova-o quando implementar sua lógica.
    elif oper == '2':
        # Chamar a função de subtrair
        pass

    elif oper == '3':
        # Chamar função de multiplicar;
        pass

    elif oper == '4':
        # Chamar operação de divisão;
        pass
    elif oper == '5':
        # Encerrar o programa com mensagem amigável
        pass
    else:
        # Escolha fora das escolhas disponíveis
        # Exibir mensagem de erro!
        pass


# Regras:
# As funções das operações devem estar em um arquivo separado chamado operacoes.py
# O arquivo principal com código da função menu deve ser chamado calculadora.py
# Para utilizar as infoções utiliza importação.


