class Forma:
    def calcular_area(self):
        pass  # Método a ser sobrescrito pelas subclasses

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return 3.14 * self.raio ** 2  # Área do círculo

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura  # Área do retângulo

# Uso do polimorfismo
circulo = Circulo(5)
print("Área do círculo:", circulo.calcular_area())

retangulo = Retangulo(4, 6)
print("Área do retângulo:", retangulo.calcular_area())
