class Livro():
    def __init__(self, id, nome, autor, status) -> None:
        self.id = id
        self.nome = nome
        self.autor = autor
        self.status = status

    def __repr__(self) -> str:
        return f'id: {self.id} \n nome: {self.nome} \n autor: {self.autor} \n status: {self.status}'


# Id? Não tem que ser dinâmico?

class Membro():
    def __init__(self, nome, cadastro) -> None:
        self.nome = nome
        self.cadastro = cadastro

rock = Membro('Rock', '12345')

class Biblioteca():
    catalogo = []
    membros = []
    # def __init__(self, nome, localidade ) -> None:
    #     self.nome = nome
    #     self.localidade = localidade

    def adicionar_novo_livro(self, Livro):
        self.catalogo.append(Livro)



minha_biblio = Biblioteca()


livro = Livro(1, 'Senhor dos Anéis', 'Tolkien', True)

minha_biblio.adicionar_novo_livro(livro)
# minha_biblio.adicionar_novo_livro(livro

print(rock.nome)