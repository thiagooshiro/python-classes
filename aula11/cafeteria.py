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
        print("\n--- Cadastro de Produto ---")
        produto_nome = input('Digite o nome do produto: ')
        produto_preco = float(input('Digite o preço do produto: R$ '))
        produto_tamanho = input('Digite o tamanho do produto (ex: pequeno, médio, grande): ')
        produto_tipo = input('Digite o tipo do produto (ex: bebida, comida, sobremesa): ')

        produto = Produto(produto_nome, produto_preco, produto_tamanho, produto_tipo)
        self.produtos.append(produto)
        print(f'Produto {produto_nome} cadastrado com sucesso!')
        return produto

    def registrar_pedido(self, cliente):
        print("\n--- Registro de Pedido ---")
        if not self.produtos:
            print("Nenhum produto cadastrado! Primeiro cadastre os produtos.")
            return
        
        print("Produtos disponíveis:")
        for i, produto in enumerate(self.produtos, 1):
            print(f"{i} - {produto}")

        produto_escolhido = input("Digite o número do produto que deseja pedir: ")

        try:
            produto_index = int(produto_escolhido) - 1
            if produto_index < 0 or produto_index >= len(self.produtos):
                print("Produto inválido!")
                return
            produto = self.produtos[produto_index]
            print(f"Pedido realizado com sucesso! Cliente: {cliente.nome} {cliente.sobrenome}")
            print(f"Produto: {produto.nome} ({produto.tipo}, {produto.tamanho}) - R$ {produto.preco:.2f}")
            return produto
        except ValueError:
            print("Opção inválida! Digite um número.")
            return None

    def listar_clientes(self):
        if not self.clientes:
            print("Nenhum cliente cadastrado.")
        else:
            print("\nClientes cadastrados:")
            for cliente in self.clientes:
                # Cada cliente será impresso com uma separação clara entre os dados
                print("\n" + str(cliente))
                print("-" * 40)  # Linha para separar cada cliente

        return None

    def listar_produtos(self):
        if not self.produtos:
            print("Nenhum produto cadastrado.")
        else:
            print("\nProdutos cadastrados:")
            for produto in self.produtos:
                print(produto)
        return None


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
            cliente = next((cli for cli in cafeteria.clientes if cli.nome == nome_cliente), None)
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
menu(cafeteria)
