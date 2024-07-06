-- @block
CREATE TABLE STUDENTS(
    id INT PRIMARY KEY AUTO_INCREMENT , 
    username VARCHAR(255) NOT NULL, 
    email VARCHAR(255) NOT NULL UNIQUE,
    class_i INT
);

-- @block