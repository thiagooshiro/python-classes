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

print(minhaCaneta.cor)

minhaCaneta.escrever('Escrevi com a minha caneta azul!')


