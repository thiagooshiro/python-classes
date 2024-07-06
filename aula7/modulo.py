def mensagem(nome):
    return f'Seja bem vindo {nome}'


try:
    x = int(input('Digite um número inteiro'))
except(ValueError):
    print(' Valor inválido')