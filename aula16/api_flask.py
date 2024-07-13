from flask import Flask, request, jsonify, render_template
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Database connection parameters
db_config = {
    'host': 'localhost',
    'database': 'school_management',
    'user': 'root',
    'password': 'in12345678'
}

def insert_student(nome, data_de_nascimento, matricula, ano):
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            with connection.cursor() as cursor:
                check_query = "SELECT * FROM estudantes WHERE matricula = %s"
                cursor.execute(check_query, (matricula,))
                existing_student = cursor.fetchone()
                if existing_student:
                    return False
                sql_insert_query = """INSERT INTO estudantes (nome, data_de_nascimento, matricula, ano)
                                      VALUES (%s, %s, %s, %s)"""
                record = (nome, data_de_nascimento, matricula, ano)
                cursor.execute(sql_insert_query, record)
                connection.commit()
                return True
    except Error as e:
        print("Error while connecting to MySQL", e)
        return False
    finally:
        if connection.is_connected():
            connection.close()

def get_all_students():
    try:
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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/students', methods=['POST'])
def api_insert_student():
    data = request.json
    nome = data['nome']
    data_de_nascimento = data['data_de_nascimento']
    matricula = data['matricula']
    ano = data['ano']
    success = insert_student(nome, data_de_nascimento, matricula, ano)
    if success:
        return jsonify({"message": "Student inserted successfully"}), 201
    else:
        return jsonify({"message": "Student already exists"}), 409

@app.route('/api/students', methods=['GET'])
def api_get_all_students():
    students = get_all_students()
    if students is not None:
        return jsonify(students), 200
    else:
        return jsonify({"message": "Error fetching students"}), 500

@app.route('/api/students/<matricula>', methods=['GET'])
def api_get_student_by_matricula(matricula):
    student = get_student_by_matricula(matricula)
    if student is not None:
        return jsonify(student), 200
    else:
        return jsonify({"message": "Student not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
