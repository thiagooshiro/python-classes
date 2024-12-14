# Guia de Sintaxe - Python

# ==========================
# 1. Listas
# ==========================
# Listas são coleções ordenadas de itens, que podem ser de tipos diferentes, e podem ser alteradas depois de criadas. 
# Elas são muito utilizadas quando precisamos armazenar múltiplos valores.

# Exemplo básico de lista:
lista = [1, 2, 3, 4, 5]  # Uma lista contendo números inteiros

# Acessando um item da lista:
print(lista[0])  # Exibe o primeiro item da lista (lembrando que o índice começa em 0, então 0 é o primeiro)

# Adicionando um item à lista:
lista.append(6)  # Adiciona o valor 6 ao final da lista
print(lista)

# Atualizando um item da lista:
lista[2] = 10  # Atualiza o valor no índice 2, que era 3, para 10
print(lista)

# Removendo um item da lista:
lista.remove(4)  # Remove o valor 4 da lista (não o índice, mas o valor)
print(lista)

# Verificando o comprimento da lista:
print(len(lista))  # Exibe o número de itens na lista

# Iterando sobre uma lista: Exibindo todos os itens da lista
for item in lista:
    print(item)

# ==========================
# 2. Loop for
# ==========================
# O loop 'for' é utilizado para iterar sobre uma sequência, como uma lista ou um intervalo de números. 
# Ele é muito utilizado quando sabemos o número de iterações de antemão.

# Exemplo 1: Iterando sobre uma lista de números
lista = [1, 2, 3, 4, 5]
for item in lista:
    print(item)  # Exibe cada item da lista

# Exemplo 2: Iterando sobre um intervalo de números utilizando range()
for i in range(5):  # O range(5) cria uma sequência de 0 a 4
    print(i)  # Exibe os números gerados pela função range()

# ==========================
# 3. Loop while
# ==========================
# O loop 'while' repete um bloco de código enquanto uma condição for verdadeira. 
# Ele é muito útil quando não sabemos o número exato de iterações que vamos precisar.

# Exemplo: Um contador que imprime de 0 a 4.
contador = 0
while contador < 5:  # O loop continuará enquanto a condição for verdadeira (contador < 5).
    print(f"Contador: {contador}")  # Exibe o valor do contador na tela.
    contador += 1  # Incrementa o valor do contador em 1 (equivalente a contador = contador + 1).

# ==========================
# 4. Estruturas Condicionais (if/elif/else)
# ==========================
# As estruturas condicionais são usadas para executar diferentes blocos de código com base em uma condição. 
# Quando a condição é verdadeira, o código dentro do bloco 'if' será executado. Se a condição do 'if' 
# não for atendida, você pode usar 'elif' para verificar outras condições, e 'else' para um bloco de código 
# a ser executado quando nenhuma das condições anteriores for verdadeira.

# Exemplo básico de if/elif/else:
condição = True

if condição:
    print("Condição verdadeira!")  # Este código será executado se a condição for verdadeira.
elif not condição:
    print("Condição falsa!")  # Este código será executado se a condição for falsa.
else:
    print("Nenhuma das condições foi atendida.")  # Se nenhuma das condições anteriores for atendida.

# ==========================
# 5. Dicionários
# ==========================
# Dicionários são coleções de pares chave-valor. Eles são úteis quando precisamos associar um valor a uma chave 
# para acessar rapidamente esse valor.

# Exemplo de criação e uso de um dicionário:
dicionario = {
    "chave1": "valor1", 
    "chave2": "valor2",
    "chave3": "valor3"
}

# Acessando um valor pelo nome da chave:
print(dicionario["chave1"])  # Exibe o valor associado à chave "chave1", ou seja, 'valor1'

# Atualizando um valor de uma chave:
dicionario["chave1"] = "novo_valor"  # Agora a chave1 vai ter o valor "novo_valor"
print(dicionario["chave1"])  # Exibe o novo valor da chave1

# Adicionando um novo item no dicionário:
dicionario["chave4"] = "valor4"  # Adiciona uma nova chave com seu valor
print(dicionario)

# Removendo um item:
del dicionario["chave2"]  # Remove a chave "chave2" e seu valor
print(dicionario)

# Iterando sobre o dicionário: Exibindo todas as chaves e seus respectivos valores.
for chave, valor in dicionario.items():
    print(f"{chave}: {valor}")  # Exibe a chave e o valor associados

# ==========================
# Dicionários com Listas
# ==========================
# É possível armazenar listas como valores em um dicionário. 
# Vamos criar um dicionário com departamentos e informações de funcionários.

dicionario_com_lista = {
    "departamento1": [
        {"nome": "João", "cargo": "Vendedor", "salário": 3000},
        {"nome": "Maria", "cargo": "Gerente", "salário": 5000}
    ],
    "departamento2": [
        {"nome": "Carlos", "cargo": "Desenvolvedor", "salário": 4000},
        {"nome": "Ana", "cargo": "Analista", "salário": 3500}
    ]
}

# Exibindo os funcionários de um departamento específico:
print("\nFuncionários do departamento1:")
for funcionario in dicionario_com_lista["departamento1"]:
    print(f"Nome: {funcionario['nome']}, Cargo: {funcionario['cargo']}, Salário: {funcionario['salário']}")
