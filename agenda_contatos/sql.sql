create database agenda_contatos;

use agenda_contatos;

create table contatos
(
    nome varchar(255),
    numero varchar(255) primary key,
    email varchar(255)
);