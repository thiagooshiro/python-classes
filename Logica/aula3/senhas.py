# senha1 = "1234"
# senha2 = "4321"
# senha3 = "1111"
# senha4 = "2222"


# if senha_digitada == senha1 or senha_digitada == senha2 or senha_digitada == senha3 or senha_digitada == senha4:
#     print('Parabéns você conseguiu acesar o sistema')


senhas_validas = ["1234" , "4321", "1111", "2222"]

print(senhas_validas[0]) # imprimir 1234, que é o primeiro item da lista;

n = 0
print(len(senhas_validas)) 
senha_digitada = input('Digite sua senha: ')

while n < len(senhas_validas):
    if senha_digitada == senhas_validas[n]:
        print('Acesso concedido')
        break
    else:
        senha_digitada = input('Senha incorreta, tente novamente: ')
    n = n + 1
    if(n == 4):
        print('Acesso Bloqueado, numero de tentativas máximas esgotado')