


def minha_func(*args):
    resultado = 0
    for el in args:
        resultado = resultado + el
    return [resultado, sum(args)]


minha_func(5, 43, 42, 2, 2)

def nova_func(**kwargs):
    return kwargs


print(nova_func(nome='Filipe', idade=17, brasileiro=True))

