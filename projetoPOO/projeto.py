class Livro():
    def __init__(self, id, titulo, autor, status) -> None:
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.status = status


class Membro():
    def __init__(self, cadastro, nome, historico) -> None:
        self.cadastro = cadastro
        self.nome = nome
        self.historico = historico


class Biblioteca():
    def __init__(self) -> None:
        self.catalago_livros = []
        self.registro_membros = []

    def adicionar_ao_catalogo(self):
        pass

    def cadastrar_membro(self):
        pass

    def pesquisar(self):
        pass

    def emprestar(self):
        pass

    def devolucao(self):
        pass



