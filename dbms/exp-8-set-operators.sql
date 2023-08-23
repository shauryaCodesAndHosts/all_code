/*union union all intersect minus*/

CREATE TABLE student1(
id INT, name VARCHAR(255), age INT );
INSERT INTO student1(id,name,age)
VALUES (1,'Devansh Sharma',21), (2,'Rahul Kalia',26), (3,'Akshat Jain',34);
CREATE TABLE students( id INT, name VARCHAR(255), age INT );

INSERT INTO students(id,name,age)
VALUES
(1,'Devansh Sharma',21),
(2,'Sarita Kumari',26),
(3,'Rohan Dubey',34);


SELECT *from student1
UNION
SELECT * from students ;

SELECT *from student1
UNION ALL
SELECT * from students;

CREATE TABLE tab1 (
Id INT PRIMARY KEY
);
INSERT INTO tab1 VALUES (1), (2), (3), (4);
CREATE TABLE tab2 (
id INT PRIMARY KEY
);
INSERT INTO tab2 VALUES (3), (4), (5), (6);

/*exectution  of intersect*/

SELECT DISTINCT Id FROM tab1
INNER JOIN tab2 USING (Id);

/* minus */

CREATE TABLE t1 ( id INT PRIMARY KEY );
CREATE TABLE t2 ( id INT PRIMARY KEY );
INSERT INTO t1 VALUES (1),(2),(3);
INSERT INTO t2 VALUES (2),(3),(4);

/*exec*/
SELECT id FROM t1
LEFT JOIN t2 USING (id)
WHERE t2.id IS NULL;

/*view */

CREATE VIEW student_data AS
SELECT s.id,s.name,c.city FROM student s INNER JOIN City c
ON s.id= c.cid; SELECT * FROM student_data ;

/*rename*/
RENAME TABLE student_data TO new_data;
SELECT * FROM new_data;

/*delete */
drop View new_data;

/*alter */
ALTER VIEW data AS
SELECT * FROM student_table
INNER JOIN City
ON student_table.city=City.cid
WHERE age>22;
SELECT *from data ;





