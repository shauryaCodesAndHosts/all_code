SELECT id, UPPER(name) AS Name ,age
FROM employee;
SELECT id, LOWER(name) AS Name ,age
FROM employee;
SELECT id,NAME, character_length(name)AS "CHARACTER LENGTH" ,age
FROM employee;
SELECT id,NAME, CONCAT(name ,age) AS CONCAT
FROM employee;
SELECT CURRENT_DATE();
SELECT NOW();
SELECT DATE("2022-04-24 23:48:15");
SELECT current_time();
SELECT current_timestamp();
SELECT localtime();
SELECT COUNT(name) FROM employee_table;
SELECT SUM(age) FROM employee_table;
SELECT AVG(age) FROM employee_table;
SELECT MAX(age) FROM employee;
SELECT MIN(age) FROM employee;