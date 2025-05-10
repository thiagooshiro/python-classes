# Transformar uma caneta em código Python.

class Caneta():
    def __init__(self, cor, marca, ponta, material, tamanho):
        self.cor = cor
        self.marca = marca
        self.ponta = ponta
        self.material = material
        self.tamanho = tamanho
    
    def escrever(self, msg):
        print(msg)



minhaCaneta = Caneta('azul', 'bic', 'esferográfica', 'plástico', '15cm')

# print(minhaCaneta.cor)

# minhaCaneta.escrever('Escrevi com a minha caneta azul!')



class Carro():  # Definição da classe
    def __init__(self, modelo, ano, cor, marca):
        self.modelo = modelo
        self.ano = ano
        self. cor = cor
        self.marca = marca

    def __str__(self):
        return f'{self.modelo}, {self.ano}, {self.cor}, {self.marca}'

    def ligarCarro(self, combustivel):
        print(f'Carro ligando com {combustivel}!')

meuCarrinho = Carro('Uno', '2021', 'Amarelo', 'FIAT') # Objeto ou Instância da classe Carro

print(meuCarrinho.modelo) #Imprime o valor contido na propriedade modelo do objeto "meuCarrinho"


print(meuCarrinho) # 

meuCarrinho.ligarCarro('gasolina') 