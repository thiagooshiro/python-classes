# Declaração de variáveis
menuzinho = 'Meu menu'

#Estrutura sintática do IF, lembrando, nem todo if tem elif e else;
if menuzinho != 'Meu menu':
    print('Erro!')
elif menuzinho == 'meu menu':
    print('bem vindo...')
else:
    print('Bem vindo')


condicao = True
while condicao:
    print('Bom dia! Escolha uma das opções:')
    print('1 - Banana')
    print('2 - Açaí')
    print('3 - Abacate')
    print('4 - Sair')
    break

#Estrutura de uma lista
frutas = ['Abacaxi', 'Maçã', 'Uva', 'Laranja', 'Tangerina', 'Manga']

# Estrutura sintática do for;
for fruta in frutas:
    print (f'A fruta {fruta} é deliciosa!')

# O For pode operar sobre variáveis que são iteráveis, a fins de simplificação, listas e também strings;

nome = 'Isabela'

for letra in nome:
    print(letra)


# O segredo do if in...
frutas = ['Abacaxi', 'Maçã', 'Uva', 'Laranja', 'Tangerina', 'Manga']
morango = "Morango"

if morango in frutas:
    print('Tem morango')
else:
    print('não tem morango T_T')

for fruta in frutas:
    if morango == fruta:
        print('Tem morango')


palavra = 'paralelepipedo'

if 'a' in palavra:
    print('tem a')