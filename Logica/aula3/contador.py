# Contar quantas letras tem a palavra que o usuário digitou:

palavra = input('Digite uma palavra')

contador = 0

#Estrutura do sintática do while:
while contador < len(palavra):
    contador += 1
    print(contador)

print(f'A palavra tem {contador} letras')