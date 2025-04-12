    
def pontuacao(escolha_jogador, escolha_maquina):
    
    if escolha_jogador == escolha_maquina:
            return 'Vocês empataram!'
        

    elif escolha_jogador == 'pedra' and escolha_maquina == 'tesoura' or escolha_jogador == 'tesoura' and escolha_maquina == 'papel' or escolha_maquina == 'papel' and escolha_maquina == 'pedra':
        return 'Parabéns! Você venceu!'

    else:
        print('Você perdeu!')
