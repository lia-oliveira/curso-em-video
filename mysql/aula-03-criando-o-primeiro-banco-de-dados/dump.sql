CREATE DATABASE IF NOT EXISTS cadastro
	DEFAULT CHARSET = utf8mb4
	DEFAULT COLLATE = utf8mb4_general_ci;

USE cadastro;

CREATE TABLE pessoas(
nome VARCHAR(30),
idade TINYINT,
sexo CHAR(1),
peso FLOAT,
altura FLOAT,
nacionalidade VARCHAR(20)
);