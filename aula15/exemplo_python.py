#Bancos de Dados, Sistemas de Gerênciamento de banco de dados (SGBDs)
# Integrando SQL com python:
# pip install mysql-connector-python

import mysql.connector
from mysql.connector import Error

# Database connection parameters
db_config = {
    'host': 'localhost',
    'database': 'school_management',
    'user': 'root',
    'password': 'In@12345678'
}


def insert_student(nome, data_de_nascimento, matricula, ano_de_ingresso, id_escola):
    try:
        # Establish the connection
        connection = mysql.connector.connect(**db_config)

        if connection.is_connected():
            with connection.cursor() as cursor:
                # Check if the student is already enrolled
                check_query = "SELECT * FROM estudantes WHERE matricula = %s"
                cursor.execute(check_query, (matricula,))
                existing_student = cursor.fetchone()

                if existing_student:
                    print(f"Student with matricula {matricula} is already enrolled.")
                    return

                # SQL query to insert a new student
                sql_insert_query = """INSERT INTO estudantes (nome, data_de_nascimento, matricula, ano_de_ingresso, id_escola)
                                      VALUES (%s, %s, %s, %s, %s)"""
                record = (nome, data_de_nascimento, matricula, ano_de_ingresso, id_escola)

                # Execute the query
                cursor.execute(sql_insert_query, record)

                # Commit the transaction
                connection.commit()
                print("Record inserted successfully into estudantes table")

    except Error as e:
        print("Error while connecting to MySQL", e)

    finally:
        if connection.is_connected():
            connection.close()


def get_all_students():
    try:
        # Establish the connection
        connection = mysql.connector.connect(**db_config)

        if connection.is_connected():
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM estudantes")
                rows = cursor.fetchall()
                return rows

    except Error as e:
        print("Error while connecting to MySQL", e)
        return None

    finally:
        if connection.is_connected():
            connection.close()

def get_student_by_matricula(matricula):
    try:
        # Establish the connection
        connection = mysql.connector.connect(**db_config)

        if connection.is_connected():
            with connection.cursor() as cursor:
                query = "SELECT * FROM estudantes WHERE matricula = %s"
                cursor.execute(query, (matricula,))
                student = cursor.fetchone()
                return student

    except Error as e:
        print("Error while connecting to MySQL", e)
        return None

    finally:
        if connection.is_connected():
            connection.close()

# Example usage for inserting a student
insert_student('Maria da Silva', '2005-05-10', 'M021', 2020, 1)

# Example usage for getting all students
students = get_all_students()
if students:
    for student in students:
        print(student)

# Example usage for getting a student by matricula
matricula = 'M021'
student = get_student_by_matricula(matricula)
if student:
    print(student)
