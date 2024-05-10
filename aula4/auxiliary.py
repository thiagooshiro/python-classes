names = ['João', 'Maria', 'Pedro', 'Ana', 'Lucas', 'Mariana', 'Gabriel', 'Julia', 'Felipe', 'Laura',
         'Matheus', 'Isabela', 'Rafael', 'Larissa', 'Gustavo', 'Carolina', 'Daniel', 'Camila', 'Vinicius', 'Amanda',
         'Guilherme', 'Natália', 'Diego', 'Bianca', 'Rodrigo', 'Letícia', 'Luciano', 'Mônica', 'Leonardo', 'Fernanda',
         'Ricardo', 'Vanessa', 'Paulo', 'Tatiane', 'Carlos', 'Bruna', 'Fábio', 'Patrícia', 'Marcelo', 'Aline', 'Alexandre',
         'Carla', 'André', 'Helena', 'Cristiano', 'Débora', 'Eduardo', 'Talita', 'Thiago', 'Roberto']


lista_matricula = [634882, 490670, 628764, 992046, 919892, 298471, 415763, 888458, 631142, 540428, 459464, 189443, 563825, 105322, 433956, 821786, 783688, 794890, 690505, 990761, 558982, 573178, 248961, 236232, 641908, 527569, 209314, 485236, 447587, 771142, 870326, 483584, 282370, 772319, 217105, 522192, 946088, 462765, 389316, 404956, 453908, 205865, 188364, 650922, 383320, 163630, 977911, 799977, 663506, 346856]

list_birthdate = ['16/07/1991', '27/04/1994', '10/12/1981', '08/03/1986', '03/08/1984', '05/12/1982', '16/03/1986', '18/03/1985', '14/10/1981', '25/12/1982', '16/08/1982', '07/07/1982', '16/09/1993', '14/04/1983', '26/12/1998', '27/02/1984', '27/01/1998', '14/07/1998', '08/03/1986', '21/04/2000', '16/08/1993', '27/06/1998', '11/07/1980', '27/10/1985', '03/01/2000', '04/05/1996', '07/12/1991', '03/03/1985', '03/12/2000', '01/11/1980', '07/07/1993', '21/06/1993', '12/10/1997', '25/06/1980', '19/10/1983', '07/01/1996', '02/06/1993', '09/12/1983', '17/04/1996', '23/05/1989', '21/05/1986', '02/03/1996', '17/09/1993', '20/04/1980', '08/09/2000', '19/11/1981', '15/10/1995', '23/12/1983', '27/08/1991', '22/01/1994']

lista_coeficiente = [ 7.9, 7.3, 6.2, 9.8, 9.7, 7.3, 8.4, 5.6, 5.7, 8.7, 9.2, 7.8, 8.7, 6.9, 9.2, 6.1, 8.9, 6.2, 5.8, 8.0, 5.8, 8.5, 9.6, 8.9, 8.5, 8.9, 5.3, 6.1, 5.5, 8.5, 9.6, 6.1, 7.2, 9.7, 6.1, 6.6, 5.2, 9.3, 7.1, 5.6, 7.3, 7.7, 6.5, 8.4, 6.0, 9.5, 8.7, 6.3, 6.7, 6.1 ]

students = []

for i in range(50):
    # Generate a birthdate between 01/01/1980 and 31/12/2000
    
    student_data = {
        'nome': names[i],
        'matrícula': lista_matricula[i],
        'data de nascimento': list_birthdate[i],
        'coeficiente acadêmico': lista_coeficiente[i]
    }
    students.append(student_data)

# print(students)

def sort_students(students_list):
    result = sorted(students_list,key= lambda x: x['coeficiente acadêmico'], reverse=True)
    lista = []
    for estudante in result:
        tupla = (estudante['nome'], estudante['coeficiente acadêmico'], estudante['matrícula'])
        lista.append(tupla)
    return result


print(sort_students(students))

    # Crie uma função que imprima a lista de nomes dos estudantes acompanhada da coeficiente acadêmico em ordem decrescente


# def coeficiente_decrecente(ordem):
#     aux = 0
#     for l in range(50):
#         for c in range(l,50):
#             if ordem[l]['coeficiente acadêmico'] < ordem[c]['coeficiente acadêmico']:
#                 aux = ordem[l]
#                 ordem[l] = ordem[c]
#                 ordem[c] = aux
#     print(ordem)
#     return ordem

# for aluno in coeficiente_decrecente(students):
#     print(f'Nome do aluno: {aluno["nome"]}')
#     print(f'Coeficiente acadêmico: {aluno["coeficiente acadêmico"]}\n')