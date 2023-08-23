CREATE TABLE teacher(t_id int primary key, name varchar(50) not null, 
qualification varchar(50) not null,salary int not null);

INSERT INTO teacher VALUES
(1,'Akshay','MCS',12000),
(2,'Amit','MBA',14000),
(3,'Aditya','MSC',13000),
(4,'Akshat','BSIT',15000),
(5,'Rahul','MPHIL',16000);

CREATE TABLE student(s_id int primary key, name varchar(50) not null,
class int not null, t_id int not null);

INSERT INTO student VALUES
(1,'Noman',11,2), (2,'Asghar',12,4),
(3,'Furqan',10,2), (4,'Khurram',11,1),
(5,'Asad',12,5), (6,'Anees',10,1),
(7,'Khalid',11,2);

SELECT t.t_id,t.name,t.qualification,s.name,s.class FROM teacher t
INNER JOIN student s
ON t.t_id= s.t_id
ORDER BY t_id,t.name;

CREATE TABLE city(
cid INT NOT NULL AUTO_INCREMENT,
cityname VARCHAR(50) NOT NULL,
PRIMARY KEY(cid)
);

INSERT INTO city(cityname)
VALUES ('Agra'), ('Delhi'), ('Bhopal'), ('Jaipur'), ('Noida');

CREATE TABLE personal( id INT NOT NULL, name VARCHAR(50) NOT NULL,
percentage INT NOT NULL, age INT NOT NULL, gender VARCHAR(1) NOT NULL,
city INT NOT NULL, PRIMARY KEY(id), FOREIGN KEY(city) REFERENCES City(cid) );

INSERT INTO personal(id,name,percentage,age,gender,city)
VALUES
(1,'Ram Kumar',45,19,"M",1),
(2,'Sarita Kumari',55,22,"M",2),
(3,'Salman Khan',62,20,"M",1),
(4,'Juhi Chawla',41,18,"M",3),
(5,'Anil Kaapoor',74,22,"M",1),
(6,'John Abraham',64,21,"M",2),
(7,'Shahid Kapoor',52,20,"M",1);

SELECT * FROM personal LEFT JOIN city
ON personal.city=city.cid;

SELECT * FROM personal LEFT JOIN city ON personal.city=city.cid UNION
SELECT * FROM personal RIGHT JOIN city
ON personal.city=city.cid;