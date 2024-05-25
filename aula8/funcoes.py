# 1 - Crie uma função que recebe uma string e imprime as letras individualmente no terminal.

# 2 - Crie uma função que recebe uma lista e imprime o primeiro e o último elemento da lista.

# 3 - Crie uma função que realiza o somatório dos valores em uma lista.

# 4 - Crie uma função que concatene um numero indefinido de caracteres.

###


# 4 - Uma empresa de automóveis está criando um sistema para cadastrar novos veículos, crie um algoritmo capaz de registrar novos veículos a partir de entradas fornecidas pelo usuário. As informações necessárias são: Modelo, ano, descrição, valor de entrada, valor de parcela e valor total. O valor de entrada é sempre 12% do valor total do veículo e o número máximo de parcelas é sempra té 18 parcelas do valor restante.




# 5 - Um supermercado está precisando de um sistema capaz de listar todos os produtos a partir de uma busca simples, o usuário deve ser capaz de procurar um produto pelo nome, parcial ou completo. Segue uma lista de exemplo:
produtos = [
    "Camiseta", "Calça jeans", "Tênis", "Mochila", "Notebook", "Fones de ouvido",
    "Smartphone", "Relógio", "Óculos de sol", "Garrafa de água", "Câmera", 
    "Console de jogos", "Livros", "Mesa", "Cadeira", "Luminária de mesa", 
    "Caderno", "Estojo", "Marcadores", "Pincéis de pintura", "Tela de pintura", 
    "Violão", "Teclado", "Microfone", "Drone", "Barraca de camping", "Saco de dormir", 
    "Botas de caminhada", "Bússola", "Lanterna", "Bicicleta", "Capacete", "Skate", 
    "Patins", "Bola de basquete", "Bola de futebol", "Taco de beisebol", 
    "Tacos de golfe", "Vara de pescar", "Raquete de tênis", "Roupa de banho", 
    "Protetor solar", "Toalha de praia", "Cesta de piquenique", "Churrasqueira", 
    "Cooler", "Jogos de tabuleiro", "Relógio de parede", "Ferro de passar roupa", 
    "Aspirador de pó", "Vaso de flores", "Chaleira", "Panela de pressão"
]

#Ex: Se o usuário digitar apenas 'c' todos os produtos que possuem a letra c devem ser listados, começando pelos que inciam pela letra procurada seguidos daqueles produtos que apenas possuem a letra c

# Caso o usuário digite uma palavra pela metade, por exemplo, "Cha" devem ser listados todos os produtos que se iniciem com esses caracteres primeiro e todos os que possuem essa sequência de caracteres em seguida.






# 6 - Uma escola precisa de um novo sistema para cadastro de estudantes, o sistema deve ser capaz de registrar novos alunos, respeitando a estrutura dos dados já existentes da escola. A lista a seguir é o exemplo da estrutura de dados utilizada pela escola. 
# Ex:
registros_alunos = [
    {
        "nome": "João Silva",
        "idade": 15,
        "classe": "9º ano",
        "notas": {"Matemática": 85, "Português": 78, "Ciências": 92, "História": 93}
    },
    {
        "nome": "Maria Oliveira",
        "idade": 14,
        "classe": "8º ano",
        "notas": {"Matemática": 90, "Português": 82, "Ciências": 88, "História": 84}
    },
    {
        "nome": "Carlos Santos",
        "idade": 16,
        "classe": "9º ano",
        "notas": {"Matemática": 78, "Português": 80, "Ciências": 75, "História": 78}
    },
    {
        "nome": "Ana Pereira",
        "idade": 15,
        "classe": "9º ano",
        "notas": {"Matemática": 92, "Português": 85, "Ciências": 90, "História": 88}
    },
    {
        "nome": "Pedro Costa",
        "idade": 14,
        "classe": "8º ano",
        "notas": {"Matemática": 88, "Português": 79, "Ciências": 84, "História": 80}
    }
]


# 6.1 Crie uma função para filtrar alunos por nome.


# 6.2 Crie uma função para filtrar alunos por ano


# 6.3 Crie uma função para filtrar alunos por desempenho em uma materia específica.





# 7 - Desafio - Uma interface de agendamento de viagens recebe as seguintes informações como demonstrado no exemplo abaixo:

# info = ["Lucas", "28", "Chile", True, "30/03/2024"]

# Faça as seguintes verificações: 
# A primeira informação não contém carater númérico.
# A segunda informação é um número.
# A terceira informação é composta por apenas uma palavra
# A quarta informação é um valor booleano
# A quinta informação não pode ser uma data que já passou.
# Caso todos os testes sejam positivos exiba a mensagem: "Viagem processada! Aguarde para impressão do ticket"
# Caso contrário imprima a mensagem: "Informações inválidas, repita o cadastro"
# Imagine que os usuários vão sempre entrar com as informações nos mais diveros formatos, teste cada um dos casos abaixo e elabore seus próprios casos:
# ex1 = ["1223", "10", "Brasil", False, "20/04/2026"]
# ex2 = ["Amanda", "24n", "França", True, "22/09/2025"]
# ex3 = ["Vitória", "33", "Marrocos", "True", "25/12/2024"]
# ex4 = ["Romero", "63", "Argentina", False, "17/03/2022" ]
# ex5 = ["matheus", "21", "Londres", True, "12/06/2024"]
# ex6 = ["JuLia", "31", "São Mateus", True, "23/04/2024"]
# ex7 = ["Venâncio", "50", "China", True, "22?05/2024"]
# ex8 = ["Maria", 23, "India", False, "07/12/2024"]
# ex9 = ["Pedro", "42", "Br4sil", True, "05/05/2024"]
# ex10 = ["Tom", 33, "Servolo", False, "02/05/1998"]