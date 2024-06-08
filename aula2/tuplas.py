# minhaTupla = ('Algo', 'Bom', 'Mais ou menos')
# minhaLista = ['Algo', 'Bom', 'Mais ou menos']

# # minhaLista[0] = 'Batata'

# print(minhaTupla[0])

# x, y, z = minhaTupla
# print(x)
# print(y)
# print(z)

# nome = 'Thiago'
# idade = 35

# nome_idade = (nome, idade)
# print(nome_idade[0])


aluno1 = ('Gabriel', [7.2, 8.4, 5.5, 10])
aluno2 = ('Flávio', [8.2, 8, 7, 6.7])
aluno3 = ('Amanda', [10, 7.2, 6.9, 8])
aluno4 = ('Bruna', [9.2, 7.4, 6.7, 7])

#Imprimir os alunos em ordem decrescente da maior MÉDIA para a menor
index = 0

media1 = sum(aluno1[1])/4
media2 = sum(aluno2[1])/4
media3 = sum(aluno3[1])/4
media4 = sum(aluno4[1])/4

alunos = [(aluno1[0], media1), (aluno2[0], media2), (aluno3[0], media3), (aluno4[0], media4)]


alunos.sort(key=lambda aluno:aluno[1], reverse=True)

print(alunos)

# media1 = sum(aluno1[1])/4
# media2 = sum(aluno2[1])/4
# media3 = sum(aluno3[1])/4
# media4 = sum(aluno4[1])/4

# alunos = [(aluno1[0], media1), (aluno2[0],media2), (aluno3[0], media3), (aluno4[0], media4)]

# alunos.sort(key=lambda x:x[1], reverse=True)
# print(alunos)

# Dada duas listas:
nomes = "Bruna", "Felipe", "Jonathan", "Marcos", "Jéssica"
sobrenomes = "Silva", "Oliveira", "Rocha", "Marques", "Amaral"
# Crie um algoritmo que imprima o nome completo de cada uma dessas pessoas;

for pessoa in zip(nomes, sobrenomes):
    print(pessoa)


# Essas listas são correspondentes, então a primeira pessoa é "Bruna" e seu sobrenome é "Silva".


amigos = [ "Anna", "Pedro", "Ramon", "Gabriel", "Lucas", "Thiago", "Val"]
presentes_favoritos = ["Livro", "Filme", "Passeio no restaurante", "Relógio", "Uma garrafa de cerveja artesanal", "Uma ida ao cinema", "Um doguinho"]

