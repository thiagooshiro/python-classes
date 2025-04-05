from random import choice


opcoes = ['pedra', 'papel', 'tesoura']


def menu():
    print('Seja bem vindo ao jogo de Pedra, Papel, Tesoura: ')
    print('Lembre-se: Pedra vence tesoura, tesoura vence papel, papel vence pedra')

    maquina = choice(opcoes)

    while True:
        escolha = input('Por favor faça sua escolha ou digite "sair" para sair do jogo: ').lower()

        if escolha == 'sair':
            print('Obrigado por jogar')
            return
        elif escolha not in opcoes:
            escolha = input('Escolha inválida, digite novamente: ')
            continue
        else:
            break

    print('Você escolheu', escolha)
    print('A máquina escolheu', maquina)


    # Lógica do jogo

    escolha = input('Deseja continuar jogando?s/n: ')
    if escolha != 'n':
        return menu()

menu()