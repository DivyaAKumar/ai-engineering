--USE SQLTutorial;
--CREATE TABLE EmployeeDemographics
--(EmpID int,
--FirstName varchar(50),
--LastName varchar(50),
--Age int,
--Gender varchar(50)
--)

--CREATE TABLE EmployeeSalary
--(EmployeeID int,
--JobTitle varchar(50),
--Salrary int)

--Insert into EmployeeDemographics VALUES
--(1001, 'Div', 'Kumar', 21, 'F'),
--(1002, 'Nav', 'Chandrakar', 23, 'M'),
--(1003, 'Harsh', 'Tiwari', 26, 'M'),
--(1004, 'Ayushi', 'Dubey', 22, 'F'),
--(1005, 'Sana', 'Uke', 25, 'F'),
--(1006, 'Nandini', 'Rishi', 23, 'F'),
--(1007, 'Harshit', 'Kumar', 27, 'M'),
--(1008, 'Parth', 'Sharma', 29, 'M'),
--(1009, 'Surya', 'Manasa', 22, 'F'),
--(1010, 'Shreya', 'Panigrahi', 20, 'F'),
--(1011, 'Mim', 'Sharma', 21, 'F')

--INSERT INTO EmployeeSalary VALUES
--(1001, 'Software Engineer', 55000),
--(1002, 'Data Analyst', 48000),
--(1003, 'Project Manager', 75000),
--(1004, 'HR Manager', 60000),
--(1005, 'Software Engineer', 58000),
--(1006, 'Data Scientist', 70000),
--(1007, 'Accountant', 50000),
--(1008, 'Sales Executive', 45000),
--(1009, 'Marketing Manager', 65000),
--(1010, 'Business Analyst', 52000),
--(1011, 'Software Engineer', 56000);

/*
select statement
top, distinct, count, as, max, min, avg
*/
Insert into EmployeeDemographics Values
(1012, 'Jam', 'pam', 27, 'M')
SELECT * FROM EmployeeDemographics

SELECT FirstName,LastName FROM EmployeeDemographics

SELECT TOP 5 * FROM EmployeeDemographics

SELECT DISTINCT(EmpID) FROM EmployeeDemographics

SELECT * FROM EmployeeSalary

--EXEC sp_rename
--'dbo.EmployeeSalary.EmployeeID',
--'EmpID',
--'COLUMN'

SELECT * FROM EmployeeSalary

SELECT COUNT(LastName) FROM EmployeeDemographics

SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE = 'BASE TABLE';

SELECT COUNT(LastName) AS LastNameCount
FROM EmployeeDemographics

SELECT * 
FROM EmployeeSalary

SELECT MAX(Salary)
FROM SQLTutorial.dbo.EmployeeSalary

/*
where statement
=,<>, <, >, And, Or, Like, Null, Not Null, In
*/

SELECT * 
FROM EmployeeDemographics
WHERE FirstName <> 'Jim' --everybody except jim


SELECT * 
FROM EmployeeDemographics
WHERE Age >= 25

SELECT * 
FROM EmployeeDemographics
WHERE Age >= 25 AND Gender = 'M'

SELECT * 
FROM EmployeeDemographics
WHERE LastName LIKE '%K'

SELECT * 
FROM EmployeeDemographics
WHERE FirstName is NOT NULL

SELECT * 
FROM EmployeeDemographics
WHERE FirstName IN ('Div', 'NAV')

/*
Group by, Order by
*/

select distinct(Gender)
from EmployeeDemographics

select Gender, Age, count(gender) as genderCount
from EmployeeDemographics
Group by Gender, Age
order by genderCount asc

select * 
from EmployeeDemographics
order by age

select * 
from EmployeeDemographics
order by age, gender desc

select * 
from EmployeeDemographics
order by age desc, gender desc
--or
select * 
from EmployeeDemographics
order by 4 desc, 5 desc

select * 
from EmployeeDemographics
order by age desc

--INTERMEDIATE SQL
--joins,unions,case statements, 
-- updating/deleting data
-- partition by
--data types
-- allasing
-- creating views
-- having vs group by statement
-- GETDATE()
-- Primary key vs foreign key

Select * 
from EmployeeDemographics

select * 
from EmployeeSalary

/*
JOINS
inner,  full/left/right outer joins
*/
--dropping current tables for better understanding


DROP TABLE IF EXISTS EmployeeDemographics;
DROP TABLE IF EXISTS EmployeeSalary;

SELECT *
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE = 'BASE TABLE';

CREATE TABLE EmployeeDemographics
(
    EmpID INT,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Age INT,
    Gender VARCHAR(50)
);

CREATE TABLE EmployeeSalary
(
    EmpID INT,
    JobTitle VARCHAR(50),
    Salary INT
);

INSERT INTO EmployeeDemographics VALUES
(1001, 'Div', 'Kumar', 21, 'F'),
(1002, 'Nav', 'Chandrakar', 23, 'M'),
(1003, 'Harsh', 'Tiwari', 26, 'M'),
(1004, 'Ayushi', 'Dubey', 22, 'F'),
(1005, 'Sana', 'Uke', 25, 'F'),
(1006, 'Nandini', NULL, 23, 'F'),
(1007, 'Harshit', 'Kumar', NULL, 'M');


INSERT INTO EmployeeSalary VALUES
(1001, 'Software Engineer', 55000),
(1002, 'Data Analyst', 48000),
(1003, 'Project Manager', 75000),
(1004, NULL, 60000),
(1005, 'Software Engineer', NULL),
(1008, 'Sales Executive', 45000),
(1009, 'Marketing Manager', 65000);


select *
from EmployeeDemographics
inner join EmployeeSalary 
on EmployeeDemographics.EmpID = EmployeeSalary.EmpID

select *
from EmployeeDemographics
full outer join EmployeeSalary 
on EmployeeDemographics.EmpID = EmployeeSalary.EmpID

select *
from EmployeeDemographics
left outer join EmployeeSalary 
on EmployeeDemographics.EmpID = EmployeeSalary.EmpID

select *
from EmployeeDemographics
right outer join EmployeeSalary 
on EmployeeDemographics.EmpID = EmployeeSalary.EmpID

