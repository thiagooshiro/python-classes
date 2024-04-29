# revisão Condicionais:

# # 31 - Crie um algoritmo que ao ser executado que verifica se um número é par ou ímpar 
# e exibe a mensagem "ímpar" se o número for ímpar e "par" se o número for par.


# if num%2 == 0:
#     print(f'o número {num} é par' )
# else:
#     print(f'O número {num} é impar')

n1 = int(input('Escreva um número'))
n2 = int(input('Escreva um número'))
n3 = int(input('Escreva um número'))

maior = n1
if n2 > maior:
    maior = n2
    if n3 > maior:
        maior = n3
        medio = n2
        menor = n1
        print(f'O maior número é {maior}')
        print(f'{medio} está entre {maior} e {menor}')
        print(f'O numero {menor} é o menor dos números fornecidos')

    elif n3 > n1:
        medio = n3
        menor = n1
        print(f'O maior número é {maior}')
        print(f'{medio} está entre {maior} e {menor}')
        print(f'O numero {menor} é o menor dos números fornecidos')
    else:
        medio = n1
        menor = n3
        print(f'O maior número é {maior}')
        print(f'{medio} está entre {maior} e {menor}')
        print(f'O numero {menor} é o menor dos números fornecidos')


elif n3 > maior:
    maior = n3
    medio = n1
    menor = n2
    print(f'O maior número é {maior}')
    print(f'{medio} está entre {maior} e {menor}')
    print(f'O numero {menor} é o menor dos números fornecidos')
elif n2 > n3:
    medio = n2
    menor = n3
    print(f'O maior número é {maior}')
    print(f'{medio} está entre {maior} e {menor}')
    print(f'O numero {menor} é o menor dos números fornecidos')

else:
    print('Há igualdades entre os elementos')

