class Aluno():
    def __init__(self, nome, endereco):
        self.__nome = nome # Propriedades privadas não podem ser acessada diretamente
        self.endereco = endereco

    def get_nome(self): # Os métodos conhecidos como "getters" servem para recuperar o valor de uma propriedade privada
        return self.__nome
    
    def set_nome(self, novo_nome): # Os métodos conhecidos como "setters" conseguem redefinir valores de propriedades privadas;
        self.__nome = novo_nome
        return self.__nome




aluno = Aluno('Amanda', 'Rua X')

# print(aluno.__nome)  <- Essa linha causa erro porque a propriedade __nome é privada.

#Para acessar o nome se utiliza a função "getter" , get_nome:
aluno.get_nome()


#Para alterar uma propriedade privada se utiliza a função "set_nome" 
print(aluno.set_nome('Julia')) 