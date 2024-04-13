#Funções em Python

estudante =  {
    'nome': 'João',
    'matrícula': 152099,
    'data de nascimento': '28/03/2000',
    'coeficiente acadêmico': 8.7
}


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

print(f'Nome: {estudante["nome"]}')
print(f'Data de Nascimento: {estudante["data de nascimento"]}')
print(f'Matrícula: {estudante["matrícula"]}')
print(f'Coeficiente Acadêmico: {estudante["coeficiente acadêmico"]}')

from auxiliary import students

print(students)

