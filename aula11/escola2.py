# Nossa escola agora passará a lidar com uma lista de estudantes a serem cadastrados e uma lista de professores a serem cadastrados
# O método que cadastra professores e alunos ainda pertence à classe Escola e deve ser executado pelo objteo da classe escola na qual desejamos cadastrar aqueles estudantes.

#Será necessario criar classes que herdam das classes originárias, para que se adequem a esse novo contexto.

# Nesse novo caso a chave "ano" corresponde ao ano de ingresso do aluno na instituição
# A chave idade foi substituida pela chave data_nascimento
from escola import Aluno

alunos = [
    {"nome": "Maria", "data_nascimento": "10/05/2005", "ano": 2023, "matricula": "A123"},
    {"nome": "João", "data_nascimento": "15/10/2002", "ano": 2024, "matricula": "B456"},
    {"nome": "Ana", "data_nascimento": "20/08/2003", "ano": 2022, "matricula": "C789"},
    {"nome": "Pedro", "data_nascimento": "25/03/2001", "ano": 2023, "matricula": "D321"},
    {"nome": "Julia", "data_nascimento": "05/12/2000", "ano": 2024, "matricula": "E654"},
    {"nome": "Lucas", "data_nascimento": "12/07/2002", "ano": 2022, "matricula": "F987"},
    {"nome": "Carla", "data_nascimento": "30/11/2003", "ano": 2023, "matricula": "G654"},
    {"nome": "Marcos", "data_nascimento": "18/09/2001", "ano": 2024, "matricula": "H321"},
    {"nome": "Lara", "data_nascimento": "28/02/2005", "ano": 2022, "matricula": "I987"},
    {"nome": "Gustavo", "data_nascimento": "08/06/2000", "ano": 2023, "matricula": "J654"}
]


professores = [
    {"nome": "Ana", "data_nascimento": "10/05/1980", "salario": 5000, "especialidade": "Ciências"},
    {"nome": "Carlos", "data_nascimento": "15/08/1975", "salario": 5500, "especialidade": "História"},
    {"nome": "Marta", "data_nascimento": "20/03/1985", "salario": 4800, "especialidade": "Português"},
    {"nome": "Pedro", "data_nascimento": "05/11/1970", "salario": 6000, "especialidade": "Matemática"}
]


class Aluno_Novo(Aluno):
    def __init__(self, nome, idade, data_nascimento, matricula) -> None:
        super().__init__(nome, idade, matricula=matricula)
        self.data_nascimento = data_nascimento


joao = Aluno_Novo('Joao', '36', '01/05/1988', 'B357')

print(hasattr(Aluno, 'ano'))



# Após realizarmos isso, continuaremos com a proposta da aula passada:

# Um professor de uma especialidade deve ser capaz de atribuir uma nota para um aluno
# Por enquanto trabalharemos assumindo que a escola possui apenas UM professor para cada disciplina.