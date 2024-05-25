minha_tupla = (1223, 'Thiago', True, 'Amanda')

# print(minha_tupla[0]

# for el in minha_tupla:
#     print(el)


nomes = ['Isabele', 'Michel', 'Renato', 'Thiago', 'Rodrigo']
outros = ('Diego', 'Maria', 'Ana')

nomes.extend(outros)
print(nomes)

notas = [8, 8.2 , 9]

nova_tupla = (nomes[0], notas[0])

# print(nova_tupla)

amigo = 'Walter'

nomes.append(amigo)

# del nomes[0]

# print(nomes)

# nomes.pop(-1)

# print(nomes)
# print(len(nomes))

nomes.insert(3, 'João')

nomes[3] = 'Rodrigo'

# print(nomes)

# print(nomes.index('Rodrigo'))