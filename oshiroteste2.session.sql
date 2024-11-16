CREATE DATABASE school_management;

-- @block
USE school_management;


-- @block
CREATE TABLE IF NOT EXISTS Escolas(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(200),
    endereco VARCHAR(255)
);

-- @block
INSERT INTO Escolas (nome, endereco) VALUES
('Escola Primária São João', 'Rua das Flores, 123'),
('Escola Secundária Santos Dumont', 'Avenida Brasil, 456'),
('Colégio Técnico de Engenharia', 'Praça da Liberdade, 789');

-- @block
-- Retorna a informação de todas as colunas da tabela escolas;
SELECT * FROM Escolas;


-- @block
-- Cria a tabela estudantes caso ela não exista;
CREATE TABLE IF NOT EXISTS estudantes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(200) NOT NULL,
    data_de_nascimento DATE,
    matricula VARCHAR(100) UNIQUE NOT NULL,
    ano_de_ingresso INT,
    id_escola INT NOT NULL,
    FOREIGN KEY (id_escola) REFERENCES Escolas(id)
);

-- @block
-- Insere os valores abaixo na tabela estudantes!
INSERT INTO estudantes (nome, data_de_nascimento, matricula, ano_de_ingresso, id_escola) VALUES
('João Silva', '2003-05-15', '12345', 2020, 1),
('Maria Souza', '2002-08-20', '23456', 2019, 1),
('Pedro Santos', '2004-01-10', '34567', 2021, 2),
('Ana Oliveira', '2003-11-25', '45678', 2020, 3),
('José Pereira', '2002-04-30', '56789', 2019, 2),
('Mariana Costa', '2004-07-05', '67890', 2021, 1),
('Carlos Rodrigues', '2003-09-12', '78901', 2020, 3),
('Beatriz Almeida', '2002-06-08', '89012', 2019, 2),
('Rafael Fernandes', '2004-03-17', '90123', 2021, 1),
('Luana Gomes', '2003-10-22', '01234', 2020, 3),
('Felipe Barbosa', '2002-02-28', '13579', 2019, 2),
('Juliana Lima', '2004-06-03', '24680', 2021, 1),
('Lucas Nunes', '2003-12-07', '35791', 2020, 3),
('Camila Santos', '2002-05-14', '46802', 2019, 2),
('Gustavo Costa', '2004-08-19', '57913', 2021, 1),
('Fernanda Oliveira', '2003-11-24', '68024', 2020, 3),
('Rodrigo Silva', '2002-07-01', '79135', 2019, 2),
('Isabela Pereira', '2004-04-16', '90246', 2021, 1),
('Marcelo Souza', '2003-09-11', '01357', 2020, 3),
('Carolina Almeida', '2002-03-27', '12468', 2019, 2);


--@block
SELECT * FROM estudantes;

--@block
INSERT INTO estudantes (nome, data_de_nascimento, matricula, ano_de_ingresso) VALUES
('Ana Maria Silva', '2005-05-10',NULL , 2020);

--@block
-- APAGA A TABELA, MUITO CUIDADO!
DROP TABLE estudantes;

--@block
-- Apaga os valores, mas não apaga a tabela. CUIDADO!
TRUNCATE TABLE estudantes;

--@block
-- SELECIONA informações da coluna nome da tabela estudantes;
-- Estrutua é sempre SELECT colunas (separadas por viruglas) FROM tabela
SELECT nome FROM estudantes;

-- @block
-- WHERE Cria um critério para a seleção, no caso, a coluna ano precisa ser maior ou igual à 2021
SELECT * FROM estudantes WHERE ano >= 2021;

--@block
-- Atualiza uma coluna de uma tabela, é importante definir um critério para atualizar, senão todas as colunas serão alteradas;
UPDATE estudantes SET nome = 'Maria Barbosa' WHERE matricula='M011';

-- @block
-- Deleta as informações da tabela segundo um critério. É IMPORTANTE SEMPRE DEFINIR UM CRITÉRIO
DELETE FROM estudantes WHERE ano < 2020 OR ano > 2021;

--@block
-- Altera o nome da coluna "ano" para "ano_de_ingresso";
ALTER TABLE estudantes
CHANGE COLUMN ano ano_de_ingresso INT;

--@block
ALTER TABLE estudantes
ADD COLUMN idade INT;


