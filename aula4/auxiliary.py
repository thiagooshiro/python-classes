import random

names = ['João', 'Maria', 'Pedro', 'Ana', 'Lucas', 'Mariana', 'Gabriel', 'Julia', 'Felipe', 'Laura',
         'Matheus', 'Isabela', 'Rafael', 'Larissa', 'Gustavo', 'Carolina', 'Daniel', 'Camila', 'Vinicius', 'Amanda',
         'Guilherme', 'Natália', 'Diego', 'Bianca', 'Rodrigo', 'Letícia', 'Luciano', 'Mônica', 'Leonardo', 'Fernanda',
         'Ricardo', 'Vanessa', 'Paulo', 'Tatiane', 'Carlos', 'Bruna', 'Fábio', 'Patrícia', 'Marcelo', 'Aline', 'Alexandre',
         'Carla', 'André', 'Helena', 'Cristiano', 'Débora', 'Eduardo', 'Talita', 'Thiago', 'Roberto']


students = []

for i in range(50):
    # Generate a birthdate between 01/01/1980 and 31/12/2000
    day = random.randint(1, 28)
    month = random.randint(1, 12)
    year = random.randint(1980, 2000)
    birthdate = f"{day:02d}/{month:02d}/{year}"
    
    student_data = {
        'nome': names[i],
        'matrícula': random.randint(100000, 999999),
        'data de nascimento': birthdate,
        'coeficiente acadêmico': round(random.uniform(5.0, 10.0), 1)
    }
    students.append(student_data)