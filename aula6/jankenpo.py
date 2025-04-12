from random import choice, randint
from logica_jogo import pontuacao

opcoes = ['pedra', 'papel', 'tesoura']

# Criar um menu
# Esse opções ao usuário, usuário escolhe uma das opções.
# Usuário escolheu, máquina escolheu.

# Vitoria do jogador.
# J -> 'Pedra' - M - 'Tesoura'
# J -> 'Papel' - M - 'Pedra'
# J -> 'Tesoura - M - 'Papel'

pontos_jogador = 0
pontos_maquina = 0
empates = 0
partidas = 0

def menu():
    global pontos_jogador
    global partidas
    global pontos_maquina
    global empates
    print('Seja bem vindo ao jogo de Pedra, Papel, Tesoura: ')
    print('Lembre-se: Pedra vence tesoura, tesoura vence papel, papel vence pedra')

    escolha_maquina = choice(opcoes)

    while True:
        escolha_jogador = input('Por favor faça sua escolha_jogador ou digite "sair" para sair do jogo: ').lower()

        if escolha_jogador == 'sair':
            print('Obrigado por jogar')
            return
        elif escolha_jogador not in opcoes:
            escolha_jogador = input('Escolha inválida, digite novamente: ')
            continue
        else:
            break

    
    print('Você escolheu', escolha_jogador)
    print('A máquina escolheu', escolha_maquina)

    # Lógica do jogo
    resultado = pontuacao(escolha_maquina, escolha_maquina)
    # Caso de Empate:
    
    print(resultado)
    partidas += 1
    escolha_jogador = input('Deseja continuar jogando?s/n: ')
    if escolha_jogador != 'n':
        return menu()
    

    # print('Você fez:', pontos_jogador)
    # print('A Máquina fez:', pontos_maquina)
    # print(f'Aconteceram {empates} empates')
    # print('Total de partidas:', partidas)



menu()

def joguinho():
    print('Jogo de advinhação:')
    escolha_jogador = int(input('A  dvinhe o número mág')) 
    numeroAleatorio = randint(0, 100)

    if escolha_jogador == numeroAleatorio:
        print('Parabéns, você venceu')
    else:
        print('Vocẽ perdeu')

