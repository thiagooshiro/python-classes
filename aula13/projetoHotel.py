import uuid
from datetime import datetime, date

class Cliente():
    def __init__(self, nome, telefone, email):
        self.id = uuid.uuid4()
        self.nome = nome
        self.telefone = telefone
        self.email = email

class Quarto():
    def __init__(self, numero, tipo, preco, status):
        self.numero = numero
        self.tipo = tipo
        self.preco = preco
        self.status = status

class Reserva():
    def __init__(self, cliente_reserva, quarto_reservado, data_check_in, data_check_out, status):
        self.cliente_reserva = cliente_reserva
        self.quarto_reservado = quarto_reservado
        self.data_check_in = data_check_in
        self.data_check_out = data_check_out
        self.status = status

class GerenciadorDeReservas():
    def __init__(self, nome_do_hotel, endereco, telefone):
        self.nome_do_hotal = nome_do_hotel
        self.endereco = endereco
        self.telefone = telefone
        self.clientes = []
        self.reservas = []
        self.quartos = []

    def validar_cadastro(self, email):
        for cliente in self.clientes:
            if email == cliente.email:
                return cliente
        return False
    
    def validar_disponibilidade(self, numero_quarto):
        for quarto in self.quartos:
            if numero_quarto == quarto.numero and quarto.status == True:
                #Se primeira condição é verdadeira O QUARTO EXISTE!!!
                # Se a segunda condição é verdadeira o quarto está disponível.
                return True
        return False


    def validar_check_in(self, data_str):
        try:
            # Tenta converter a string para data no formato brasileiro
            data_check_in = datetime.strptime(data_str, '%d/%m/%Y').date()

            # Verifica se a data é hoje ou no futuro
            if data_check_in < date.today():
                print('❌ A data de check-in não pode ser no passado.')
                return None

            return data_check_in

        except ValueError:
            print('❌ Data inválida. Use o formato DD/MM/AAAA.')
            data_corrigida = input('Digite a data no formado correto: ')
            return self.validar_check_in(data_corrigida)
        

    def validar_check_out(self, data_check_in, data_check_out_str):
        try:
            # Converte apenas a data de check-out
            data_check_out = datetime.strptime(data_check_out_str, '%d/%m/%Y').date()

            # Verifica se o check-out é depois do check-in
            if data_check_out <= data_check_in:
                print('❌ A data de check-out deve ser depois do check-in.')
                nova_data = input('Digite uma nova data de check-out (DD/MM/AAAA): ')
                return self.validar_check_out(data_check_in, nova_data)

            return data_check_out

        except ValueError:
            print('❌ Data inválida. Use o formato DD/MM/AAAA.')
            nova_data = input('Digite uma nova data de check-out (DD/MM/AAAA): ')
            return self.validar_check_out(data_check_in, nova_data)


    def cadastrar_cliente(self):
        print("\n--- Cadastro de Cliente ---")
        cliente_nome = input('Digite seu nome: ')
        cliente_email = input('Digite seu e-mail: ')
        cliente_telefone = input('Digite seu telefone: ')

        cliente = Cliente(cliente_nome, cliente_telefone, cliente_email )
        self.clientes.append(cliente)
        print(f'Cliente {cliente_nome} cadastrado com sucesso!')
        return cliente
    
    def cadastrar_quarto(self):
        print('-------- CADASTAR QUARTOS ------- ')
        numero_quarto = input('Digite o número do quarto: ')
        tipo_quarto = input('Digite o tipo do quarto: ')
        preco_quarto = input('Digite o valor da diária do quarto: ')
        status_quarto = True

        quarto = Quarto(numero_quarto, tipo_quarto, preco_quarto, status_quarto)
        print(f'Quarto {numero_quarto} cadastrado com sucesso!!!')
        self.quartos.append(quarto)
        return quarto
    
    def cadastrar_reserva(self):
        email_reserva = input('Digite o email do cliente cadastrado: ')
        # verificar se o cliente existe no cadastro
        validar_cliente =  self.validar_cadastro(email_reserva)

        if validar_cliente == False:
            print('Usuário não cadastrado')
            print('Por favor cadastre o cliente')
            return
        
        numero_quarto_reservado = input('Digite o número do quarto a ser reservado')
        # validar se o quarto existe e se ele está disponível

        validar_quarto = self.validar_disponibilidade(numero_quarto_reservado)

        if validar_quarto == False:
            print('Quarto não existente ou ocupado')
            print('Tente novamente...')
            return self.cadastrar_reserva()
        
        data_check_in = input('Digite a data do check in (DD/MM/AAAA): ')
        # Verificar se a data do check in é válida...
        verifica_check_in = self.validar_check_in(data_check_in)

        data_check_out = input('Digite a data do check out')
        
        # Validar data do checkout:
        validar_check_out = self.validar_check_out(verifica_check_in, data_check_out)

        
        status = True
        reserva = Reserva(validar_cliente, numero_quarto_reservado, data_check_in, data_check_out)
        print('Parabéns, reserva realizada com sucesso!')
        print(f'O Quarto {numero_quarto_reservado} estará diponível para check in em {data_check_in}')
        print(f'A data de check out é {data_check_out}')

        return reserva


    def alterar_reserva(self):
        pass

    def cancelar_reserva(self):
        pass

    def listar_reservas(self):
        pass

  
    
    

    



joao = Cliente('João', '3', 'joao@email.com')

print(joao.id)


quartão = Quarto(420, 'Muito grande', 1200, True)



