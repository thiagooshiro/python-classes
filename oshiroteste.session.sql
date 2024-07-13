CREATE DATABASE school_management;

USE school_management


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
SELECT * FROM escolas


-- @block

CREATE TABLE IF NOT EXISTS estudantes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(200),
    data_de_nascimento DATE,
    matricula VARCHAR(100),
    ano INT
);

-- @block

INSERT INTO estudantes (nome, data_de_nascimento, matricula, ano) VALUES
('Ana Maria Silva', '2005-05-10', 'M001', 2020),
('Carlos Eduardo Santos', '2006-11-22', 'M002', 2021),
('Beatriz Oliveira', '2004-03-15', 'M003', 2019),
('Daniela Ferreira', '2005-09-30', 'M004', 2020),
('Eduardo Lima', '2003-07-12', 'M005', 2018),
('Fernanda Souza', '2004-01-25', 'M006', 2019),
('Gabriel Alves', '2006-08-19', 'M007', 2021),
('Heloisa Carvalho', '2005-12-05', 'M008', 2020),
('Igor Costa', '2003-04-17', 'M009', 2018),
('Julia Pereira', '2006-06-30', 'M010', 2021),
('Leonardo Martins', '2005-02-10', 'M011', 2020),
('Mariana Rocha', '2004-10-21', 'M012', 2019),
('Nicolas Gomes', '2003-11-03', 'M013', 2018),
('Olivia Santos', '2006-05-18', 'M014', 2021),
('Pedro Henrique Barros', '2004-07-09', 'M015', 2019),
('Quirino Andrade', '2005-09-14', 'M016', 2020),
('Raquel Menezes', '2003-08-02', 'M017', 2018),
('Samuel Duarte', '2006-10-25', 'M018', 2021),
('Thais Silva', '2004-12-28', 'M019', 2019),
('Vinicius Ribeiro', '2005-03-06', 'M020', 2020);

--@block
SELECT * FROM estudantes


-- @block
SELECT nome FROM estudantes WHERE id = 1


