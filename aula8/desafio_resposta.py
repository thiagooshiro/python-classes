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

def search_products(query):
    matching_products = []
    for product in produtos:
        if query.lower() in product.lower():
            matching_products.append(product)
    return matching_products

# Example usage:
query = input("Enter your search query: ")
matching_products = search_products(query)
if matching_products:
    print("Matching products:")
    for product in matching_products:
        print(product)
else:
    print("No products found matching the search query.")
=======

>>>>>>> b2ec8ad03236e761f410b82e6c67c4b6e25f8c9b
