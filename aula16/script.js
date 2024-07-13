document.getElementById('add-student-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    const nome = document.getElementById('nome').value;
    const data_de_nascimento = document.getElementById('data_de_nascimento').value;
    const matricula = document.getElementById('matricula').value;
    const ano = document.getElementById('ano').value;

    const response = await fetch('/api/students', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ nome, data_de_nascimento, matricula, ano })
    });

    const result = await response.json();
    alert(result.message);
});

async function fetchAllStudents() {
    const response = await fetch('127.0.0.1:5000/api/students');
    const students = await response.json();
    const studentsList = document.getElementById('students-list');
    studentsList.innerHTML = '';
    students.forEach(student => {
        const li = document.createElement('li');
        li.textContent = `Nome: ${student[1]}, Data de Nascimento: ${student[2]}, Matrícula: ${student[3]}, Ano: ${student[4]}`;
        studentsList.appendChild(li);
    });
}
