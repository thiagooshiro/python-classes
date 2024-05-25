def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b, menu):
    if b > 0:
        return a/b
    else:
        print('Não é possível dividir por 0,  escolha novamente os valores que deseja dividir')
        return menu()


