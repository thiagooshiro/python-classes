class Cachorro():
    def __init__(self, raca, idade, nome) -> None:
        self.nome = nome
        self.idade = idade
        self.raca = raca

    def latir(self):
        print('AU AU')

    def comer(self):
        msg = f'{self.nome} está comendo'
        print(msg)
        return msg

    def correr(self):
        print(f'{self.nome} está correndo')        


floquinho = Cachorro('poodle', 15, 'Floquinho')


floquinho.comer()

