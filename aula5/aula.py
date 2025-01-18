#Lembrando:

#Exemplo estrutura sintática do if:
condicao = int(input('Digite um numero'))
if condicao == 0:
    print('Comportamento')
    print('Bom dia')
elif condicao > 0:
    print('comportamento elif')
    print('boa tarde')
else:
    print('Comportamento de exceção')


# Resolução exercício dos 3 numeros:
# Crie uma algoritmo que recebe 3 valores e define: qual é o maior entre eles, qual é o menor e qua está entre eles;

num1 = int(input('Digite o primeiro número '))
num2 = int(input('Digite o segundo número '))
num3 = int(input('Digite o terceiro número '))

a = 0
b = 0
c = 0
if a < b and a < c:
    menor = a
    if b < c:
        intermediario, maior = b, c
    else:
        intermediario, maior = c, b
elif b < a and b < c:
    menor = b
    if a < c:
        intermediario, maior = a, c
    else:
        intermediario, maior = c, a
else:
    menor = c
    if a < b:
        intermediario, maior = a, b
    else:
        intermediario, maior = b, a

print(menor, intermediario, maior)


# Exemplo laço de repetição com While:

controle = 0
while controle < 5:
    print('Legal!')
    controle += 1 # Esse incremento precisa ser feito porque senão a condição de saída do while nunca será cumprida resultando num loop infinito.


amigos = ['Bruna', 'João', 'Luís', 'Amanda']
palavra = 'abacate'

for amigo in amigos:
    print(amigo.upper())

for letra in palavra:
    print(letra.upper())


numeros = [1, 2 ,3, 4, 5, 6 , 7, 8 , 9 , 10]
# Utilize for para imprimir só os pares;
for num in numeros:
    if num % 2 == 0:
        print(num)

print('Range e loop')
#Imprima apenas números divisiveis por 4 entre 0 e 50, considerando o range definido abaixo.
for n in range(0, 51, 2):
    if n % 4 == 0:
        print(n)


# Funções

def saudar(nome):
    print(f'Seja bem vinda, {nome}')

saudar('Isabela')



def soma_das_notas(a, b, c ,d):
    resultado = a + b + c + d
    return resultado

# calcular a média:
resultado = soma_das_notas(10, 8.4, 4.5, 7)/4

print(resultado)

# lista de tarefas (com while)

print('Seja bem vinda(o) à lista de tarefas')
while True:
    print('Digite: ')
    print('1 - Para adicionar novas tarefas')
    print('2 - Para listar todas as tarefas')
    print('3 - Para deletar a última tarefa')
    print('4 - Digite 4 para sair ')

    escolha = input('Digite sua escolha: ')

    if escolha == '1':
        print('Tarefa adicionada')
    elif escolha == '2':
        print('Tarefas: ')
    elif escolha == '3':
        print('Tarefa removida')
    elif escolha == '4':
        print('Volte sempre!')
        break
    else:
        print('Escolha inválida, selecione uma das opções fornecidas')



# lista de tarefas (com def)


def menu_tarefas(nome):
    print(f'Olá, {nome}')
    print('1 - Para adicionar novas tarefas')
    print('2 - Para listar todas as tarefas')
    print('3 - Para deletar a última tarefa')
    print('4 - Digite 4 para sair ')

    escolha = input('Digite sua escolha: ')

    if escolha == '1':
        print('Tarefa adicionada')
    elif escolha == '2':
        print('Tarefas: ')
    elif escolha == '3':
        print('Tarefa removida')
    elif escolha == '4':
        print('Volte sempre!')
    else:
        print('Escolha inválida, selecione uma das opções fornecidas')

    if escolha != '4':
        return menu_tarefas(nome)

import random

num = random.randint(0, 10)

print(num)