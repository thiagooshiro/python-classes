class Produto:
    def __init__(self, nome, preco, tamanho, tipo):
        self.nome = nome
        self.preco = preco
        self.tamanho = tamanho
        self.tipo = tipo

    def __str__(self):
        return f"{self.nome} ({self.tipo}, {self.tamanho}) - R$ {self.preco:.2f}"


class Cliente:
    def __init__(self, nome, sobrenome, endereco, email, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.endereco = endereco
        self.email = email
        self.senha = senha

    def __str__(self):
        # Ajustando a formatação para exibir de maneira mais clara no terminal
        return f"Nome: {self.nome} {self.sobrenome}\nEmail: {self.email}\nEndereço: {self.endereco}\n"


class Cafeteria:
    def __init__(self, nome, endereco, cnpj):
        self.nome = nome
        self.endereco = endereco
        self.cnpj = cnpj
        self.clientes = []
        self.produtos = []

    def cadastrar_cliente(self):
        print("\n--- Cadastro de Cliente ---")
        cliente_nome = input('Digite seu nome: ')
        cliente_sobrenome = input('Digite seu sobrenome: ')
        cliente_endereco = input('Digite seu endereço: ')
        cliente_email = input('Digite seu e-mail: ')
        cliente_senha = input('Digite sua senha: ')

        cliente = Cliente(cliente_nome, cliente_sobrenome, cliente_endereco, cliente_email, cliente_senha)
        self.clientes.append(cliente)
        print(f'Cliente {cliente_nome} {cliente_sobrenome} cadastrado com sucesso!')
        return cliente

    def cadastrar_produto(self):
       pass

    def registrar_pedido(self, cliente):
        pass

    def listar_clientes(self):
        pass

    def listar_produtos(self):
        pass


# Função do menu
def menu(cafeteria):
    print('\nBem-vindo ao sistema da Cafeteria Fabulosa!')
    print('Escolha uma das opções abaixo:')
    print('1 - Cadastrar novos clientes')
    print('2 - Listar clientes cadastrados')
    print('3 - Cadastrar produtos')
    print('4 - Listar produtos cadastrados')
    print('5 - Realizar pedido')
    print('6 - Sair')

    escolha = input('Escolha uma opção: ')
    
    if escolha == '1':
        cafeteria.cadastrar_cliente()
        return menu(cafeteria)  # Chama o menu novamente após o cadastro do cliente

    elif escolha == '2':
        cafeteria.listar_clientes()  # Chama o método listar_clientes()
        return menu(cafeteria)  # Chama o menu novamente após a listagem dos clientes

    elif escolha == '3':
        cafeteria.cadastrar_produto()
        return menu(cafeteria)  # Chama o menu novamente após o cadastro do produto

    elif escolha == '4':
        cafeteria.listar_produtos()  # Chama o método listar_produtos()
        return menu(cafeteria)  # Chama o menu novamente após a listagem dos produtos

    elif escolha == '5':
        if not cafeteria.clientes:
            print("Nenhum cliente cadastrado para realizar o pedido.")
        else:
            nome_cliente = input("Informe o nome do cliente para realizar o pedido: ")
            cliente = None
            for cli in cafeteria.clientes:
                if cli.nome == nome_cliente:
                    cliente = cli
                    break
            
            if not cliente:
                print(f"Cliente {nome_cliente} não encontrado.")
                return menu(cafeteria)  # Chama o menu novamente caso o cliente não seja encontrado
            else:
                cafeteria.registrar_pedido(cliente)
                return menu(cafeteria)  # Chama o menu novamente após o pedido

    elif escolha == '6':
        print("Saindo... Até logo!")
        return  # Encerra a função e sai do programa

    else:
        print("Opção inválida, tente novamente.")
        return menu(cafeteria)  # Chama o menu novamente caso a opção seja inválida


# Exemplo de uso:
cafeteria = Cafeteria("Café Central", "Rua Principal, 100", "12345678000199")

cafeteria2 = Cafeteria("Café Descomunal", "Rua Ábobora", '4')

menu(cafeteria)
