from random import randint



segredo = randint(1, 100)
tentativa = 0
while tentativa != segredo:
    tentativa = int(input('Digite um número'))
    if tentativa != segredo:
        print('Tente novamente.. hehehe')   
print('Ah..  cabou =(')

