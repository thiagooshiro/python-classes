# Declaração de Variáveis

copo = 'água'  #essa é uma variável do tipo string

altura = 1.82  #essa é uma variável do tipo float (ponto flutuante), numero real;

idade = 22  #Essa é uma variável do tipo inteiro;

brasileiro = True #Essa é uma variável do tipo booleano;


#Operadores de comparações
print(4 == 4) # True

print(7 < 3) # False

print(3 <= 5) # True

print(4 > 5) # False

print(16 >= 16) # True

print(4 != 5) #True


#Operações Aritimeticas
print(altura + idade) # Soma

print(idade - 42) # Subtração

print(altura * 2)  # Multiplicação

print(31 / 5) # 31.2 (Divisão comum)

print(3 ** 2) # 9  (Potenciação)

print(25 // 6) # 4 (Divisão inteira)

print(25 % 2) # 1  (Módulo de, ou resto da divisão inteira)


#Outros Operadores Lógicos:

chuva = False
fim_de_semana = True


# AND
print(chuva == False and fim_de_semana == True) 

#Funcionamento Operador AND é "exclusivo" qualquer operador "False" resultará em "False" na saída
print (False and False) # False
print (True and False) # False
print (False and True) # False
print (True and True) # True


#Funcionamento do Operador OU

print (False or False) #  False
print (True or False) # True
print(False or True) # True
print(True or True) # True


