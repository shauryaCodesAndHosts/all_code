CREATE DATABASE AKASH;
USE AKASH;

CREATE TABLE employee_TABLE(
id int NOT NULL AUTO_INCREMENT,
name varchar(45) NOT NULL,
occupation varchar(35) NOT NULL,
age int NOT NULL, PRIMARY KEY (id)
);

DROP TABLE employee_table;

CREATE TABLE employee(
id int NOT NULL AUTO_INCREMENT,
name varchar(45) NOT NULL,
occupation varchar(35) NOT NULL,
age int NOT NULL,
PRIMARY KEY (id));

ALTER TABLE employee
MODIFY Occupation varchar(35)
AFTER age;

ALTER table employee
DROP column occupation;

ALTER table employee
ADD city VARCHAR(255);

TRUNCATE TABLE employee;
