def soma(a, b):
    print(a+b)

# soma(3, 2)


def multiplica(x, y):
    resultado = x * y
    return resultado


numA = 22
numB = 33

# print(multiplica(numA, numB))

# Segundo exercício material

def horario(hora):
    if hora > 6 and hora < 12:
        print('Bom dia!')
    elif hora > 12 and hora < 18:
        print('Boa tarde!')
    else:
        print('Boa noite')


horario(17)