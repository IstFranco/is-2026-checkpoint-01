CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    legajo VARCHAR(20),
    feature VARCHAR(20),
    servicio VARCHAR(50),
    estado VARCHAR(20)
);

INSERT INTO members (nombre, apellido, legajo, feature, servicio, estado)
VALUES
('Franco', 'Oyhenart', '33555', '01', 'infraestructura-base' , 'activo')
('Esteban', 'Trillo', '33728', '02', 'frontend', 'activo'),
('Franco', 'Oyhenart', '12346', '03', 'backend', 'activo'),
('Brenda', 'Conti', '33717', '04', 'database', 'activo')
('Lautaro', 'Flores', '33411', '05', 'portainer', 'activo');
