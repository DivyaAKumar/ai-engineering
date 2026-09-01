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
