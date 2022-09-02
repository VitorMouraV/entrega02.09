create database reclamacao;
use reclamacao;

create table pessoa(
codigo int not null primary key auto_increment,
nome varchar(120) not null,
telefone varchar(15) not null,
endereco varchar(220) not null,
dataDeNascimento date not null
) engine = InnoDB;

create table reclamacao(
codigo int not null primary key auto_increment,
locall varchar(120),
numero varchar(10),
reclamacao varchar(220)
)engine = InnoDB;

select * from reclamacao;
select * from pessoa;