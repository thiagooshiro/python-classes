def soma(a, batata):
    return a + batata

def subtracao(a, b):
    return a - b

def multiplicao(a, b):
    return a * b

def divisao(a, b=1):
    return a/b
        

def calculadora(oper, numA, numB):
    print('Bem vindos à calculadora')
    print('Para escolher uma operação digite um valor entre 1 e 4')
    print('1. Soma', '2. Subtração', '3. Multiplicação', '4. Divisão', sep='\n')
    oper = input('Qual operação você deseja realizar?')
    a = input('Digite')

def soma_tudo(*args):
    result = 0
    for num in args:
        result += num
    return result

# print(soma_tudo(2, 3, 4, 5, 19, 42, 27), 'abobora', sep='\n')
# def mostrar_info(**kwargs):
#     for chave, valor in kwargs.items():
#         print(f'{chave}: {valor}')

# mostrar_info(nome='João', idade="30",altura=170)

# print(divisao(10))

# numeros = [1, 2, 3 ,4 ,5]

# quadrados = list(map(lambda x: x**2, numeros))

# print(quadrados)

from functools import reduce

# somatorio = reduce(soma, numeros)
# print(somatorio)

def concatenar(*args):
    result = ''
    for letra in args:
        result += letra
    return result

# print(concatenar('b', 'a', 'n', 'a', 'n', 'a'))

def maiorstring(a, b):
    print(a, b)
    if len(a) > len(b):
        return a
    else:
        return b
    

produtos = ["aveia", "maçã", "uva", "abobora", "leite", "pão", "sabonete", "desodorante", "amaciante", "chuveiro", "amoreira", "azulejo"]
maior = reduce(maiorstring, produtos)
print(maior)

