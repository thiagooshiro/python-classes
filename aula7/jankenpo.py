from random import randint


opcoes = ['pedra', 'papel', 'tesoura']

aleatorio = randint(0, 2)
print(opcoes[aleatorio])




# Criar um menu
# Esse opções ao usuário, usuário escolhe uma das opções.
# Usuário escolheu, máquina escolheu.

# Vitoria do jogador.
# J -> 'Pedra' - M - 'Tesoura'
# J -> 'Papel' - M - 'Pedra'
# J -> 'Tesoura - M - 'Papel'



def joguinho():
    print('Jogo de advinhação:')
    escolha = int(input('A  dvinhe o número mág')) 
    numeroAleatorio = randint(0, 100)

    if escolha == numeroAleatorio:
        print('Parabéns, você venceu')
    else:
        print('Vocẽ perdeu')

