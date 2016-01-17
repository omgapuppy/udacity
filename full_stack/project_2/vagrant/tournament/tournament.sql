-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
-- @author Ardi Mehist

CREATE TABLE player  ( id serial primary key,
                       name varchar (25) not null,
                       created timestamp default current_timestamp );

CREATE TABLE match   ( id serial primary key,
                       winner int,
                       loser int,
                       foreign key (winner) references player(id),
                       foreign key (loser) references player(id) );
