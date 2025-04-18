# Curso MySQL #04 - Melhorando a Estrutura do Banco de Dados

# Criação do schema
CREATE DATABASE cadastro
DEFAULT CHARACTER SET utf8mb4
DEFAULT COLLATE utf8mb4_general_ci;

# Criação de tabelas
CREATE TABLE pessoas (
	`id` INT NOT NULL AUTO_INCREMENT,
	`nome` VARCHAR(30) NOT NULL,
    `nascimento` DATE,
    `sexo` ENUM('M','F'),
    `peso` decimal(5,2),
    `altura` decimal (3, 2),
    `nacionalidade` VARCHAR(20) DEFAULT 'Brasil',
     PRIMARY KEY (id)
)DEFAULT CHARSET utf8;

# Coloca a base de dados em uso
USE cadastro;