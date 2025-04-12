SELECT Alunos.nome AS aluno, Escolas.nome AS escola
FROM Alunos
INNER JOIN Escolas ON Alunos.id_escola = Escolas.id;

SELECT nome, id_escola
FROM Alunos
WHERE id_escola = 1;


SELECT 
  Alunos.nome AS nome_aluno,
  Escolas.nome AS nome_escola
FROM 
  Alunos
INNER JOIN 
  Escolas ON Alunos.id_escola = Escolas.id
WHERE 
  Alunos.id_escola = 1;
  
SELECT 
  Alunos.nome AS nome_aluno,
  Escolas.nome AS nome_escola
FROM 
  Alunos 
LEFT JOIN 
  Escolas 
ON 
  Alunos.id_escola = Escolas.id;
  
  
  
SELECT 
  Alunos.nome AS nome_aluno,
  Escolas.nome AS nome_escola
FROM 
  Escolas
RIGHT JOIN 
  Alunos ON Escolas.id = Alunos.id_escola;



SELECT 
  Alunos.nome AS nome_aluno,
  Escolas.nome AS nome_escola
FROM 
  Escolas
RIGHT JOIN 
  Alunos ON Escolas.id = Alunos.id_escola;


SELECT * From Alunos WHERE id_escola = 3 LIMIT 3;



