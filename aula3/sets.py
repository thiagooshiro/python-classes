meuSet = {'segunda', 'terça', 'quarta' }


# adiciona um novo valor no set
meuSet.add('miercoles') 

# atualiza o set com novos valores de uma lista 
meuSet.update(['outro']) 

# verifica se o valor "segunda" existe no set "meuSet"
print('segunda' in meuSet) 


# Removem valores do set "meuSet", o valor removido é a string dentro dos parenteses
meuSet.remove('segunda')
meuSet.discard('segunda feira')
print(meuSet)

meuSet = {'segunda', 'terça', 'quarta', 'quinta' }
outro_set = {'terça', 'quarta'}

# Cria um novo set que é a interseção dos conjuntos "meuSet" e "outro_set"
novo_set = meuSet.intersection(outro_set)
print(novo_set)

#Cria uma união entre "meuSet" e "outro_set"
uniao = meuSet.union(outro_set)
print(uniao)

