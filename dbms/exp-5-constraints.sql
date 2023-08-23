CREATE TABLE EMPLOYEE (
id INT,
name VARCHAR(50),
age INT,
gender varchar(10),
city VARCHAR(10)
);
2. INSERT INTO employee (id, name, age, gender)
VALUES
(1, 'Akash', 21, 'M'),
(2, 'Adarsh', 22, 'M'),
(3, 'Divansh', 18, 'M'),
(4, 'Ayush', 19, 'M'),
(5, 'Mayank', 24, 'M');
3. alter table employee add constraint pri primary key(id);
4. alter table employee add constraint one unique(id);
5. Select * from employee;
6. create table dept(dept_no int(10), dept_name varchar(20));
alter table dept add constraint depn primary key (dept_name);
