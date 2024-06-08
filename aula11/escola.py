class Aluno():
     
    def __init__(self, nome, idade,matricula, ano=None) -> None:
        self.nome = nome
        self.idade = idade
        self.ano = ano
        self.matricula = matricula
        self.notas = {} # estrutura do registro da nota (dict, cujo os valores das chaves são listas com as notas)
    
    def gritar(self):
        return f'O aluno {self.nome} gritou'
    
    def __str__(self) -> str:
        return f" Nome: {self.nome}, Matrícula: {self.matricula}"



class Professor():
    def __init__(self, nome, idade, salario, especialidade):
        self.nome = nome,
        self.idade = idade,
        self.salario = salario
        self.especialidade = especialidade
    # pra professor poder lançar a nota para 1 aluno específico.

class Escola():
    escolas = []
    def __init__(self, nome, endereco, segmento):
        self.nome = nome
        self.endereco = endereco
        self.segmento = segmento
        self.matriculados = []

    
    def matricular(self):
        print('Cadastro de Novo Aluno:')
        nome = input('Digite o nome do aluno')
        idade = input('Digite a idade do aluno')
        ano = input('Digite o ano em que o aluno está matriculado')
        matricula = input('Digite o número de matricula do estudante')
        aluno = Aluno(nome, idade, ano, matricula)
        self.matriculados.append(aluno)

    def cadastrar_professor(self):
        pass
    
    def get_matriculados(self):
        alunos = ''
        for item in self.matriculados:
            alunos += str(item) + ','
        return alunos

# class EscolaNova(Escola):
#     def __init__(self, nome, endereco, segmento, area, numero_cadastro, civil_militar):
#         super().__init__(nome, endereco, segmento)
#         self.area = area
#         self.numero_cadastro = numero_cadastro,
#         self.civil_militar = civil_militar
    
#     def casdatrar_funcionarios(self):
#         pass
        

# 1 -Cadastre uma escola, registre um professor de matemática, história, ciências e português

# 2 - Verifique a lista de profesores cadastrados

# 3 - Matricule 5 alunos

# 4 - Lance notas (pelo menos 3) de cada materia para cada aluno matriculado.

# escola = Escola('Ab', 'ba', 'b')

# escola.matricular()
# escola.matricular()
# print(escola.get_matriculados())
# print(escola.matriculados[0].gritar())


# escola2 = Escola('Ba', 'ba', 'b')
# print(escola2.get_matriculados(), 'bobiei')