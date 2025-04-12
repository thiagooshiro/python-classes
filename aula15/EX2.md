1. SELECT com INNER JOIN:
Selecione o nome dos alunos e o nome da escola em que estão matriculados.

2. SELECT com LEFT JOIN:
Selecione todos os alunos, incluindo aqueles que não estão matriculados em nenhuma escola.

3. UPDATE com INNER JOIN:
Atualize o nome da escola do aluno de ID 5 para "Escola Nova".

4. DELETE com WHERE:
Exclua todos os alunos que não estão matriculados em nenhuma escola (sem id_escola).

5. SELECT com WHERE e JOIN:
Selecione o nome dos alunos e o nome das escolas, mas só mostre os alunos que estão matriculados em escolas públicas.

6. UPDATE com LEFT JOIN:
Atualize o status de todos os alunos que estão matriculados em escolas inativas para "Transferido".

7. SELECT com JOIN e ORDER BY:
Selecione o nome e a cidade dos alunos, juntamente com o nome da escola, ordenando os resultados pela cidade.

8. DELETE com JOIN:
Exclua todas as escolas que não têm nenhum aluno matriculado.

9. SELECT com múltiplos JOINS:
Selecione o nome do aluno, nome da escola e o telefone da escola. Exiba apenas alunos que têm data de nascimento posterior a 2000.

10. UPDATE com JOIN e WHERE:
Atualize o nome da escola para "Escola Melhor" onde a escola do aluno com id 8 seja "Escola Antiga".

11. SELECT com COUNT e GROUP BY:
Selecione o número de alunos matriculados em cada escola, juntamente com o nome da escola.

12. DELETE com WHERE e NOT EXISTS:
Exclua todas as escolas que não têm alunos matriculados.

13. UPDATE com CASE:
Atualize o status dos alunos para "Graduado" se a data de matrícula for anterior a 2015. Caso contrário, mantenha o status como "Ativo".

14. SELECT com LEFT JOIN e WHERE:
Selecione todos os alunos e o nome da escola, mas somente mostre alunos que têm um status ativo.

15. INSERT com SELECT e JOIN:
Crie uma nova escola e insira todos os alunos com id_escola = NULL nessa escola recém-criada.

16. SELECT com JOIN e LIKE:
Selecione o nome dos alunos e o nome da escola onde o nome da escola contém a palavra "Pública".

17. DELETE com JOIN e LIMIT:
Exclua 5 alunos que estão com status "Inativo" e não têm nenhuma escola associada a eles.

18. UPDATE com JOIN e SET múltiplos campos:
Atualize o nome de um aluno e a cidade da escola associada a ele. O nome do aluno é "Carlos" e o nome da escola é "Escola Estadual".

19. SELECT com INNER JOIN e subconsulta:
Selecione o nome dos alunos que estão matriculados em escolas que têm mais de 50 alunos.

20. DELETE com JOIN, WHERE e LIMIT:
Exclua os alunos com status "Transferido" de escolas que têm menos de 5 alunos matriculados.