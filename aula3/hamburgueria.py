hamburguer1 = ['X-Beleza', 'parmesão', 'costelão', 'alface', 'tomate', 'molho especial', 'mussarela']


x_beleza = {
    "nome": 'X-Beleza',
    "pão": "parmesão",
    "carne": "costelão",
    "queijo": "canastra",
    "salada": ["alface, tomate", "cebola"],
    "especiais": "molho especial"
}


x_beleza['gostoso'] = True
x_beleza['nome'] = "X gostosão"


print(x_beleza)


hamburgers = [
    {
    "nome": 'X-Beleza',
    "pão": "parmesão",
    "carne": "costelão",
    "queijo": "canastra",
    "salada": ["alface, tomate", "cebola"],
    "especiais": "molho especial"
},
{
    "nome": 'X-Bomdia',
    "pão": "francês",
    "carne": "frango desfiado",
    "queijo": "mussarela",
    "salada": ["alface, tomate", "alho", "manejericão"],
    "especiais": "molho especial, bacon, ovo"
}
]


for item in hamburgers:
    item['vegetariano'] = False


lista_alunos = [{'nome': 'Ana', 'matrícula': 992046, 'data de nascimento': '08/03/1986', 'coeficiente acadêmico': 9.8}, {'nome': 'Lucas', 'matrícula': 919892, 'data de nascimento': '03/08/1984', 'coeficiente acadêmico': 9.7}, {'nome': 'Tatiane', ': 'Diego', 'matrícula': 248961, 'data de nascimento': '11/07/1980', 'coeficiente acadêmico': 9.6}, {'nome': 'Ricardo', 'matrícula': 870326, 'data de nascimento': '07/07/1993', 'coeficiente acadêmico': 9.6}, {'nome': 'Débora', 'matrícula': 163630, 'data de nascimento': '19/11/1981', 'coeficiente acadêmico': 9.5}, {'nome': 'Patrícia', 'matrícula': 462765, 'data de nascimento': '09/12/1983', 'coeficiente acadêmico': 9.3}, {'nome': 'Matheus', 'matrícula': 459464, 'data de nascimento': '16/08/1982', 'coeficiente acadêmico': 9.2}, {'nome': 'Gustavo', 'matrícula': 433956, 'data de nascimento': '26/12/1998', 'coeficiente acadêmico': 9.2}, {'nome': 'Daniel', 'matrícula': 783688, 'data de nascimento': '27/01/1998', 'coeficiente acadêmico': 8.9}, {'nome': 'Bianca', 'matrícula': 236232, 'data de nascimento': '27/10/1985', 'coeficiente acadêmico': 8.9}, {'nome': 'Letícia', 'matrícula': 527569, 'data de nascimento': '04/05/1996', 'coeficiente acadêmico': 8.9}, {'nome': 'Laura', 'matrícula': 540428, 'data de nascimento': '25/12/1982', 'coeficiente acadêmico': 8.7}, {'nome': 'Rafael', 'matrícula': 563825, 'data de nascimento': '16/09/1993', 'coeficiente acadêmico': 8.7}, {'nome': 'Eduardo', 'matrícula': 977911, 'data de nascimento': '15/10/1995', 'coeficiente acadêmico': 8.7}, {'nome': 'Natália', 'matrícula': 573178, 'data de nascimento': '27/06/1998', 'coeficiente acadêmico': 8.5}, {'nome': 'Rodrigo', 'matrícula': 641908, 'data de nascimento': '03/01/2000', 'coeficiente acadêmico': 8.5}, {'nome': 'Fernanda', 'matrícula': 771142, 'data de nascimento': '01/11/1980', 'coeficiente acadêmico': 8.5}, {'nome': 'Gabriel', 'matrícula': 415763, 'data de nascimento': '16/03/1986', 'coeficiente acadêmico': 8.4}, {'nome': 'Helena', 'matrícula': 650922, 'data de nascimento': '20/04/1980', 'coeficiente acadêmico': 8.4}, {'nome': 'Amanda', 'matrícula': 990761, 'data de nascimento': '21/04/2000', 'coeficiente acadêmico': 8.0}, {'nome': 'João', 'matrícula': 634882, 'data de nascimento': '16/07/1991', 'coeficiente acadêmico': 7.9}, {'nome': 'Isabela', 'matrícula': 189443, 'data de nascimento': '07/07/1982', 'coeficiente acadêmico': 7.8}, {'nome': 'Carla', 'matrícula': 205865, 'data de nascimento': '02/03/1996', 'coeficiente acadêmico': 7.7}, {'nome': 'Maria', 'matrícula': 490670, 'data de nascimento': '27/04/1994', 'coeficiente acadêmico': 7.3}, {'nome': 'Mariana', 'matrícula': 298471, 'data de nascimento': '05/12/1982', 'coeficiente acadêmico': 7.3}, {'nome': 'Alexandre', 'matrícula': 453908, 'data de nascimento': '21/05/1986', 'coeficiente acadêmico': 7.3}, {'nome': 'Paulo', 'matrícula': 282370, 'data de nascimento': '12/10/1997', 'coeficiente acadêmico': 7.2}, {'nome': 'Marcelo', 'matrícula': 389316, 'data de nascimento': '17/04/1996', 'coeficiente acadêmico': 7.1}, {'nome': 'Larissa', 'matrícula': 105322, 'data de nascimento': '14/04/1983', 'coeficiente acadêmico': 6.9}, {'nome': 'Thiago', 'matrícula': 663506, 'data de nascimento': '27/08/1991', 'coeficiente acadêmico': 6.7}, {'nome': 'Bruna', 'matrícula': 522192, 'data de nascimento': '07/01/1996', 'coeficiente acadêmico': 6.6}, {'nome': 'André', 'matrícula': 188364, 'data de nascimento': '17/09/1993', 'coeficiente acadêmico': 6.5}, {'nome': 'Talita', 'matrícula': 799977, 'data de nascimento': '23/12/1983', 'coeficiente acadêmico': 6.3}, {'nome': 'Pedro', 'matrícula': 628764, 'data de nascimento': '10/12/1981', 'coeficiente acadêmico': 6.2}, {'nome': 'Camila', 'matrícula': 794890, 'data de nascimento': '14/07/1998', 'coeficiente acadêmico': 6.2}, {'nome': 'Carolina', 'matrícula': 821786, 'data de nascimento': '27/02/1984', 'coeficiente acadêmico': 6.1}, {'nome': 'Mônica', 'matrícula': 485236, 'data de nascimento': '03/03/1985', 'coeficiente acadêmico': 6.1}, {'nome': 'Vanessa', 'matrícula': 483584, 'data de nascimento': '21/06/1993', 'coeficiente acadêmico': 6.1}, {'nome': 'Carlos', 'matrícula': 217105, 'data de nascimento': '19/10/1983', 'coeficiente acadêmico': 6.1}, {'nome': 'Roberto', 'matrícula': 346856, 'data de nascimento': '22/01/1994', 'coeficiente acadêmico': 6.1}, {'nome': 'Cristiano', 'matrícula': 383320, 'data de nascimento': '08/09/2000', 'coeficiente acadêmico': 6.0}, {'nome': 'Vinicius', 'matrícula': 690505, 'data de nascimento': '08/03/1986', 'coeficiente acadêmico': 5.8}, {'nome': 'Guilherme', 'matrícula': 558982, 'data de nascimento': '16/08/1993', 'coeficiente acadêmico': 5.8}, {'nome': 'Felipe', 'matrícula': 631142, 'data de nascimento': '14/10/1981', 'coeficiente acadêmico': 5.7}, {'nome': 'Julia', 'matrícula': 888458, 'data de nascimento': '18/03/1985', 'coeficiente acadêmico': 5.6}, {'nome': 'Aline', 'matrícula': 404956, 'data de nascimento': '23/05/1989', 'coeficiente acadêmico': 5.6}, {'nome': 'Leonardo', 'matrícula': 447587, 'data de nascimento': '03/12/2000', 'coeficiente acadêmico': 5.5}, {'nome': 'Luciano', 'matrícula': 209314, 'data de nascimento': '07/12/1991', 'coeficiente acadêmico': 5.3}, {'nome': 'Fábio', 'matrícula': 946088, 'data de nascimento': '02/06/1993', 'coeficiente acadêmico': 5.2}]
