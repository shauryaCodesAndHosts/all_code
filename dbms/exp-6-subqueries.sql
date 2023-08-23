CREATE TABLE department(
dept_id INT PRIMARY KEY,
dept_name VARCHAR(50)
);
2. INSERT INTO department VALUES
(1,'H-R'),
(2,'Finance'),
(3,'Accounts'),
(4,'Administration'),
(5,'Counselling');
3. CREATE TABLE employee(
emp_id INT PRIMARY KEY,
name VARCHAR(500),
gender VARCHAR(50),
age INT,
salary INT,
dept_id INT,
FOREIGN KEY(dept_id)
REFERENCES department(dept_id)
);
INSERT INTO employee VALUES
(1,'Ali','M',23,24000,3),
(2,'Anup','M',24,25000,4),
(3,'Akshay','M',22,22000,1),
(4,'Akshat','M',21,65000,2),
(5,'Rahul','M',23, 22000,4);
5. SELECT * from employee
WHERE dept_id =(SELECT dept_id FROM department
WHERE dept_name='H-R');
6. CREATE TABLE department(
id INT primary key,
name varchar(100) NOT NULL,
gender varchar(50) NOT NULL,
city varchar(20) NOT NULL,
salary int NOT NULL
);
7. INSERT INTO department(id,name,gender,city,salary) VALUES
(1,'Ram Kumar','M','Rajasthan',12000),
(2,'Neeraj Singh','M','MP',15000),
(3,'Devansh Sharma','M','Delhi',30000),
(4,'Rahul Kalia','M','UP',40000),
(5,'Akshat Jain','M','UP',50000);
8. SELECT * from department where id
IN(SELECT id from department where salary>12000);
9. SELECT * from department where id
IN(SELECT max(salary) from department);
10. SELECT count(name) AS COUNT from department
where name=(select count(salary)>10000 from department);