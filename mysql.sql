create database instituto;

use instituto;


CREATE TABLE estudiante (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(30),
    apellido VARCHAR(30),
    edad INT,
    mail VARCHAR(30),
    matricula VARCHAR(30),
    carrera VARCHAR(30)
);


INSERT INTO estudiante (nombre, apellido, edad, mail, matricula, carrera) VALUES
('Juan', 'Pérez', 20, 'juan@example.com', 'MAT1234', 'Ingeniería Civil'),
('María', 'García', 22, 'maria@example.com', 'MAT5678', 'Psicología'),
('Pedro', 'Martínez', 21, 'pedro@example.com', 'MAT91011', 'Administración'),
('Laura', 'López', 23, 'laura@example.com', 'MAT121314', 'Derecho'),
('Carlos', 'Sánchez', 19, 'carlos@example.com', 'MAT151617', 'Medicina');



select * from estudiante  