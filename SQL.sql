-- B A S I C S --
-- CRUD Operations

-- C R E A T E
CREATE DATABASE test;

-- DELETE Database
DROP DATABASE test;

-- there are multiple database so to access any specific one
USE test;

-- create table
CREATE TABLE employee(
                      name char(10),
                      salary int,
                      department char
                      email varchar
);
-- creating new table by selecting col from existing table
CREATE TABLE new_table AS
SELECT salary, department
FROM employee;


-- DELETE Table (two ways)
DROP TABLE employee;  --entire table will be deleted
TRUNCATE TABLE employee;  --only data inside table will be deleted



-- A L T E R
-- add col in table
ALTER TABLE employee
ADD age int;

-- delete col
ALTER TABLE employee
DROP email;

-- changing datatype of col
ALTER TABLE employee
ALTER COLUMN salary float;
MODIFY COLUMN salary float;  --this works in MySQL/Oracle



-- SQL Operations --
-- Constraints (to make some rules to limit the data type)
CREATE DATABASE cartoon;

USE cartoon;


-- 1. NOT NULL
CREATE TABLE Doraemon(
                      ID int NOT NULL,  --this field cannot be null
                      Name char,
                      Address varchar(100),
                      Age int
);
ALTER TABLE Doraemon
ALTER COLUMN Name char NOT NULL;



-- 2. UNIQUE
ALTER TABLE Doraemon
ALTER COLUMN Age int NOT NULL UNION;  --no duplicate values

ALTER TABLE Doraemon
ALTER COLUMN ID int PRIMARY KEY;

-- using constrains while creating table
--for SQL server/Oracle/MS Access
CREATE TABLE Shinchan(
                      ID int NOT NULL UNIQUE,  --same for primary key
                      Name char UNIQUE,
                      Address varchar(100),
                      Age int
);
--for MySQL
CREATE TABLE Shinchan(
                      ID int NOT NULL,
                      Name char,
                      Address varchar(100),
                      Age int,
                      UNIQUE(ID,Name,Address)
);



-- 3. PRIMARY KEY (both not null & unique)
-- table can have only one primary key
--on creating table
CREATE TABLE Shinchan(
                      ID int NOT NULL,
                      Name char,
                      Address varchar(100),
                      Age int,
                      PRIMARY KEY(ID)
);
--on altering tabel
ALTER TABLE Shinchan
ADD PRIMARY KEY(Age);

--you can have multiple primary key
--on creating table
CREATE TABLE Shinchan(
                      ID int NOT NULL,
                      Name char,
                      Address varchar(100),
                      Age int,
                      CONSTRAINT MULTI_PK PRIMARY KEY(ID,Name,Address)
);
--on altering tabel
ALTER TABLE Shinchan
ADD CONSTRAINT MULTI_PK PRIMARY KEY(Age, ID, Address);  --MULTI_PK(container name in which all the PK is stored)

-- DROP a PRIMARY KEY
ALTER TABLE Persons
DROP PRIMARY KEY;  --u can also add CONSTRAINT after DROP to delete



-- 4. FOREIGN KEY
--A FOREIGN KEY is a field (or collection of fields) in one table, that refers to the PRIMARY KEY in another table.
--on creating table
CREATE TABLE Persons (
    PersonID int NOT NULL,
    LastName char NOT NULL,
    FirstName char NOT NULL,
    Age int NOT NULL,
    PRIMARY KEY (PersonID),
);
CREATE TABLE Orders (
    OrderID int NOT NULL,
    OrderNumber int NOT NULL,
    PersonID int,
    PRIMARY KEY (OrderID),
    FOREIGN KEY (PersonID) REFERENCES Persons(PersonID)
);
--on altering tabel
ALTER TABLE Orders
ADD FOREIGN KEY (PersonID) REFERENCES Persons(PersonID);

--you can have multiple primary key
--on creating table
CREATE TABLE Orders (
    OrderID int NOT NULL,
    OrderNumber int NOT NULL,
    PersonID int,
    PRIMARY KEY (OrderID),
    CONSTRAINT FK_PersonOrder FOREIGN KEY (PersonID,...if)
    REFERENCES Persons(PersonID)
);
--on altering tabel
ALTER TABLE Orders
ADD CONSTRAINT FK_PersonOrder FOREIGN KEY (PersonID,...if) REFERENCES Persons(PersonID);

--DROP a FOREIGN KEY
ALTER TABLE Orders
DROP FOREIGN KEY FK_PersonOrder;  --u can also add CONSTRAINT after DROP to delete



-- 4. CHECK
-- The CHECK constraint is used to limit the value range that can be placed in a column.
--on creating table
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    CHECK (Age>=18)
);
--on altering table
ALTER TABLE Persons
ADD CHECK (Age>=18);

-- multiple CHECK
--on creating table
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    City varchar(255),
    CONSTRAINT CHK_Person CHECK (Age>=18 AND City='Sandnes')
);
--on altering table
ALTER TABLE Persons
ADD CONSTRAINT CHK_PersonAge CHECK (Age>=18 AND City='Sandnes');



-- 5. DEFAULT
--The DEFAULT constraint is used to set a default value for a column.
--The default value will be added to all new records, if no other value is specified.
--on creating table
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    City varchar(255) DEFAULT 'Sandnes'
);
--system values can also be added
CREATE TABLE Orders (
    ID int NOT NULL,
    OrderNumber int NOT NULL,
    OrderDate date DEFAULT GETDATE()
);
--on altering table
ALTER TABLE Persons
ALTER City SET DEFAULT 'Sandnes';

--delete
ALTER TABLE Persons
ALTER COLUMN City DROP DEFAULT;



-- 6. CREATE INDEX
--The CREATE INDEX statement is used to create indexes in tables.
--Indexes are used to retrieve data from the database more quickly than otherwise.
SYNTAX: CREATE INDEX index_name
        ON table_name (column1, column2, ...);

--example
CREATE INDEX idx_lastname
ON Persons (LastName);
--create an index on a combination of columns
CREATE INDEX idx_pname
ON Persons (LastName, FirstName);

-- unique index
CREATE UNIQUE INDEX index_name
ON table_name (column1, column2, ...);



-- Entering datas into the table
CREATE TABLE Employee(
                      ID int,
                      Name char(20) NOT NULL,
                      Salary int NOT NULL,
                      Experience int NOT NULL,
                      PRIMARY KEY(ID)
);
--entering data
INSERT INTO Employee(ID, Name, Salary, Experience)
VALUES(1, "Bhavin", 50000, 1);
INSERT INTO Employee(ID, Name, Salary, Experience)
VALUES(2, "Kevin", 50000, 1);
INSERT INTO Employee(ID, Name, Salary, Experience)
VALUES(3, "Radhika", 40000, 0);
INSERT INTO Employee(ID, Name, Salary, Experience)
VALUES(4, "Babita", 500, 0);
INSERT INTO Employee(ID, Name, Salary, Experience)
VALUES(5, "Ravi", 10000, 2);

--if no field is nullable, below given is the another way to enter the data
INSERT INTO Employee()
VALUES(1, "Bhavin", 50000, 1),
VALUES(3, "Radhika", 40000, 0),
VALUES(4, "Babita", 500, 0);

--AUTO_INCREMENT keyword automatically increment ID
--it only works on field which is Primary Key
CREATE TABLE Employee(
                      ID int AUTO_INCREMENT,
                      Name char(20) NOT NULL,
                      Salary int NOT NULL,
                      Experience int NOT NULL,
                      PRIMARY KEY(ID)
);
INSERT INTO Employee(Name, Salary, Experience)  --ID will be auto incremented
VALUES("Bhavin", 50000, 1),
VALUES("Radhika", 40000, 2),
VALUES("Babita", 500, 0);



-- S E L E C T
SELECT * FROM Employee;  --it will select whole table
--to select specific col
SELECT Name, Salary FROM Employee;

-- DISTINCT keyword
SELECT DISTINCT Salary FROM Employee;  --all the unique values will be selected

-- WHERE keyword (satisfy conditions)
SELECT Salary FROM Employee
WHERE Salary BETWEEN 500 AND 1000;  --here it includes the starting & ending range
--other conditional symbols [>, <, >=, <=, =, !=/<>]

--to find pattern we use LIKE keyword
SELECT Email FROM Employee
WHERE Email LIKE "@gmail.com";

-- operators for condition [AND, OR, NOT]
SELECT Salary FROM Employee
WHERE Salary BETWEEN 10 AND 100;

SELECT Salary FROM Employee
WHERE NOT Salary > 100;

SELECT Salary FROM Employee
WHERE Salary > 10 OR Salary > 50;



-- U P D A T E
--altering/modify is always used for table
--update is used for data
UPDATE Employee
SET Name = "Bhavin"
WHERE ID = 1;



-- D E L E T E
-- 2 types of delete hard and soft
--in soft delete data will not be visible but it will be stored SET SQL_SAFE_UPDATES=1; & perform query
--in hard data will be removed permanently SET SQL_SAFE_UPDATES=0; & perform query
DELETE FROM Employee
WHERE Experience < 2;



-- ORDER BY (sorting) [default is ASC & can change it to DESC]
SELECT Salary FROM Employee
ORDER BY Salary;

SELECT * FROM Employee
ORDER BY Name DESC;

-- sorting by multiple condition
SELECT Experience FROM Employee
ORDER BY Name, Age;  --here if the name is same than it will sort according to the age



-- MAX & MIN keyword
SELECT MAX(Salary) FROM Employee;
SELECT MIN(Age) FROM Employee;

SELECT MAX(Salary) FROM Employee
WHERE Age BETWEEN 25 AND 35;

SELECT MAX(Name) FROM Employee;  --here name will be sort according to the ASCII value of char



-- COUNT keyword  (total no. of rows)
SELECT COUNT(Salary) FROM Employee;

SELECT COUNT(Salary) FROM Employee
WHERE Age > 25;



-- AVG keyword
SELECT AVG(Salary) FROM Employee;

SELECT AVG(Salary) FROM Employee
WHERE Age > 30;



-- SUM keyword
SELECT SUM(Salary) FROM Employee;

SELECT SUM(Salary) FROM Employee
WHERE Age > 30;



-- Wildcards ['%', '_', '[]', '^', '-', '{}']  ** Supported only in Oracle databases.
--The '%' wildcard represents any number of characters, even zero characters.
--returns all the info whose email id matches with the gmail
SELECT * FROM Employee
WHERE Email LIKE '%gmail%';

--return all the info whose names starts with 'B' & end with 'n'
SELECT * FROM Employee
WHERE Name LIKE 'B%n';

--The '_' wildcard represents a single character.
--return all info whose name starts with any char but followed by 'havin'
SELECT * FROM Employee
WHERE Name LIKE '_havin';

--The '[]' wildcard returns a result if any of the characters inside gets a match.
SELECT * FROM Employee
WHERE Name LIKE '[bsp]%';

--The '-' wildcard allows you to specify a range of characters inside the '[]' wildcard.
SELECT * FROM Employee
WHERE Name LIKE '[a-f]%';



-- J O I N S
--A JOIN clause is used to combine rows from two or more tables, based on a related column between them.
--Here are the different types of the JOINs in SQL
--1.(INNER) JOIN: Returns records that have matching values in both tables
--2.LEFT (OUTER) JOIN: Returns all records from the left table, and the matched records from the right table
--3.RIGHT (OUTER) JOIN: Returns all records from the right table, and the matched records from the left table
--4.FULL (OUTER) JOIN: Returns all records when there is a match in either left or right table

CREATE TABLE Employee(
                      EID int AUTO_INCREMENT,
                      EName char(100) NOT NULL,
                      City char(50) NOT NULL,
                      PRIMARY KEY(EID)
);
CREATE TABLE Department(
                      DID int AUTO_INCREMENT,
                      DName char(100) NOT NULL,
                      EID int,
                      PRIMARY KEY(DID)
);

INSERT INTO Employee(EName, City)
VALUES
("Bhavin", "Navsari"),
("Kevin", "Navsari"),
("Rushang", "Surat"),
("Radhika", "Virndawan"),
("Stuti", "Ahmedabad");

INSERT INTO Department(DName, EID)
VALUES
("HR", 5),
("Sales", 2),
("Marketing", 9),
("HR", 1),
("IT", 7),
("IT", 6);

--NOTE:- the data will be sorted according to the table which occurs first
-- INNER JOIN (common b/w table)
SELECT * FROM Employee
INNER JOIN Department
On Employee.EID = Department.EID;


-- LEFT OUTER JOIN (common from table 2 & entire table 1)
SELECT * FROM Employee
LEFT JOIN Department
On Employee.EID = Department.EID;


-- RIGHT OUTER JOIN (entire table 2 & matched values from table 1)
SELECT * FROM Employee
RIGHT JOIN Department
On Employee.EID = Department.EID;


-- FULL OUTER JOIN (entire table whether it match with left or right side)
--in MySQL we cannot perform this is syntax of sql
SELECT * FROM Employee
FULL OUTER JOIN Department
On Employee.EID = Department.EID;

--for MYSQL use keyword 'UNION'
SELECT * FROM Employee
LEFT JOIN Department
On Employee.EID = Department.EID;
UNION
SELECT * FROM Employee
RIGHT JOIN Department
On Employee.EID = Department.EID;


-- the below given query will create single col combining all distinct values
SELECT EName FROM Employee
UNION
SELECT DName FROM Department;
-- the below given query will create two col combining all values even if it has duplicate values
SELECT EName, EID FROM Employee
UNION ALL
SELECT DName, DID FROM Department;
