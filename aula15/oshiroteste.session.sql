-- @block
CREATE TABLE STUDENTS(
    id INT PRIMARY KEY AUTO_INCREMENT , 
    username VARCHAR(255) NOT NULL, 
    email VARCHAR(255) NOT NULL UNIQUE,
    class_i INT
);

-- @block
INSERT INTO Students.students(username, email, class_i)
VALUES (
    'oshiroteste',
    'teste@email.com',
    32
)

-- @block

SELECT * FROM students