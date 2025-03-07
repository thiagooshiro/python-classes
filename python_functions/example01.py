# Em Python, uma função é um bloco de código que realiza uma tarefa específica.
# A função pode receber parâmetros (valores de entrada) e retornar um valor ou realizar uma ação.

# Sintaxe básica para definir uma função:
# def nome_da_funcao(parâmetro1, parâmetro2):
#     # Bloco de código
#     resultado = parâmetro1 + parâmetro2
#     return resultado

# Definindo a função 'somar' que recebe dois parâmetros (a e b)
# e retorna a soma dos dois valores.
def somar(a, b):
    # A operação abaixo soma os valores passados como parâmetros.
    return a + b

# Chamando a função 'somar' com os argumentos 3 e 5
# A função irá retornar a soma de 3 + 5, que é 8.
resultado = somar(3, 5)

# Imprimindo o resultado da soma, que será 8
# A função 'print' exibe o valor retornado pela função 'somar'
print(resultado)  # Vai imprimir 8
