# Listas em Python


# minhaLista = ['Bruna', 'Luiz', 'João', 'Andressa', 'Rogério']

# # Imprimam:

# # Primeiro valor da lista

# # Segundo valor da lista

# # Terceiro valor da lista.

# # Cada valor individual da lista através de um loop for.

# # Adicionem um novo valor a esta lista utilizando método .append()
# minhaLista.append('Gustavo')

# print(minhaLista[-1])

# # O método "insert" insere um novo valor na lista, na posição definida no primeiro argumento.
# minhaLista.insert(2, 'Thiago')
# print(minhaLista)

# # Método .pop remove um valor lista via indice ou o último indice caso nenhum indice seja informado.

# minhaLista.pop(2)
# print(minhaLista)

# # Método .remove tira um valor específico da lista.

# minhaLista.remove('Bruna')
# print(minhaLista)

produtos = ["aveia", "maçã", "uva", "abobora", "leite", "pão", "sabonete", "desodorante", "amaciante", "chuveiro"]

contador = 0
for item in produtos:
    contador += 1
    if item[0] == 'a':
        # produtos.insert(contador, 'banana')
        produtos.insert(produtos.index(item) + 1, 'banana')
