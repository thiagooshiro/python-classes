#Funções em Python
# estudante = ['João', 152099, '12/03/2000', 8.7]
# 

estudante =  {
    'nome': 'João',
    'matricula': 152099,
    'data_nascimento': '28/03/2000',
    'coeficiente_academico': 8.7
}

# Cria uma copia do dicionário estudante
estudante2 = estudante.copy()

# Altera o valor da chave "nome"
estudante['nome'] = 'Mariana' 

# Adiciona a chave cursos e suas informações
estudante['cursos'] = ['Matemática', 'Física', 'Biologia'] 

# del estudante['cursos'] #remove a chave cursos

estudante.pop('matricula') # remove a chave matrícula


print(estudante.keys()) # retorna as chaves que o dicionário possui.

print(list(estudante)) # cria uma lista composta pelas chaves do dicionário
print(len(estudante)) #retorna o numero de chaves do dicionário

print('nome' in estudante) #verifica se existe a chave "nome" no dicionário estudante

print(estudante.get('nome')) # retorna o valor contido na chave "nome" do dicionário estudante

print(estudante.items()) # retorna uma lista de tuplas combinando chave e valor do dicionário.

outras_infos = {
    'nome': 'Thiago',
    'local_nascimento': 'Ouro Preto',
    'nacionalidade': 'Brasileiro',
    'estado_civil': 'solteiro'
}

estudante.update(outras_infos)   # atualiza as informações do dicionario e adiciona chaves não existentes com seus respectivos valores
print(estudante)
# Imprima o valor da chave "nome" do dicionário "estudante"
# print(estudante['nome'])

# Imprima o valor de 'matrícula' do dicionário "estudante"
# print(estudante['matrícula'])

# Imprima o valor de data de nascimento do dicionário "estudante"
# print(estudante['data de nascimento'])

# Imprima o valor de "coeficiente acadêmico" do dicionário "estudante"
# print(estudante['coeficiente acadêmico'])

# Imprima os valores das chaves do dicionário no seguinte formato:
# Nome: 
# Data de Nascimento:
# Matricula:
# Coeficiente Acadêmico:

# print(f'Nome: {estudante["nome"]}')
# print(f'Data de Nascimento: {estudante["data de nascimento"]}')
# print(f'Matrícula: {estudante["matrícula"]}')
# print(f'Coeficiente Acadêmico: {estudante["coeficiente acadêmico"]}')

# from auxiliary import students

# print(students)

