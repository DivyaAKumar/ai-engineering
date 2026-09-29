-- ============================================================
-- PostgreSQL Learning
-- SQL Practice Queries
-- ============================================================


-- ============================================================
-- 1. CREATE TABLE
-- ============================================================

CREATE TABLE person (
    id INT NOT NULL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(150) UNIQUE,
    gender VARCHAR(20) NOT NULL,
    dob DATE NOT NULL,
    country VARCHAR(50) NOT NULL
);


-- ============================================================
-- 2. ALTER TABLE
-- ============================================================

-- Add NOT NULL constraint
ALTER TABLE person
ALTER COLUMN first_name SET NOT NULL;

-- Add PRIMARY KEY
ALTER TABLE person
ADD PRIMARY KEY (id);

-- Add a new column
ALTER TABLE person
ADD COLUMN email VARCHAR(150);

-- Change column data type
ALTER TABLE person
ALTER COLUMN id TYPE BIGINT;


-- ============================================================
-- 3. IMPORT SQL FILE
-- ============================================================

-- Import an SQL file from psql
-- \i 'C:/Users/divya/Downloads/person.sql'

-- Set date format before importing dates such as MM/DD/YYYY
SET datestyle = 'MDY';


-- ============================================================
-- 4. BASIC SELECT
-- ============================================================

-- Select all columns
SELECT *
FROM person;

-- Select specific columns
SELECT id, first_name, last_name, email
FROM person;


-- ============================================================
-- 5. ORDER BY
-- ============================================================

-- Sort first names in ascending order
SELECT *
FROM person
ORDER BY first_name;

-- Sort first names in descending order
SELECT *
FROM person
ORDER BY first_name DESC;

-- Sort multiple columns
SELECT id, first_name, last_name, email
FROM person
ORDER BY first_name DESC, email DESC;

-- First name ascending, date of birth descending
SELECT *
FROM person
ORDER BY first_name, dob DESC;

-- Get the first 10 rows after sorting
SELECT *
FROM person
ORDER BY first_name DESC
LIMIT 10;


-- ============================================================
-- 6. DISTINCT
-- ============================================================

-- Get unique countries
SELECT DISTINCT country
FROM person;

-- Get unique countries sorted descending
SELECT DISTINCT country
FROM person
ORDER BY country DESC;


-- ============================================================
-- 7. WHERE
-- ============================================================

-- Filter by country
SELECT *
FROM person
WHERE country = 'India';

-- Filter by gender
SELECT *
FROM person
WHERE gender = 'Male';


-- ============================================================
-- 8. AND / OR
-- ============================================================

-- AND
SELECT *
FROM person
WHERE gender = 'Male'
AND country = 'India';

-- OR
SELECT *
FROM person
WHERE country = 'India'
OR country = 'Japan';


-- ============================================================
-- 9. COMPARISON OPERATORS
-- ============================================================

SELECT *
FROM person
WHERE id = 10;

SELECT *
FROM person
WHERE id <> 10;

SELECT *
FROM person
WHERE id > 100;

SELECT *
FROM person
WHERE id < 100;

SELECT *
FROM person
WHERE id >= 100;

SELECT *
FROM person
WHERE id <= 100;


-- ============================================================
-- 10. LIMIT / OFFSET / FETCH
-- ============================================================

-- Return 10 rows
SELECT *
FROM person
LIMIT 10;

-- Skip first 10 rows and return the next 10
SELECT *
FROM person
LIMIT 10
OFFSET 10;

-- FETCH alternative
SELECT *
FROM person
FETCH FIRST 10 ROWS ONLY;


-- ============================================================
-- 11. IN
-- ============================================================

-- Find people from selected countries
SELECT *
FROM person
WHERE country IN ('India', 'China', 'Japan');

-- NOT IN
SELECT *
FROM person
WHERE country NOT IN ('India', 'China', 'Japan');


-- ============================================================
-- 12. BETWEEN
-- ============================================================

-- BETWEEN is inclusive
SELECT *
FROM person
WHERE id BETWEEN 100 AND 200;

-- Date range
SELECT *
FROM person
WHERE dob BETWEEN DATE '2022-01-01'
              AND DATE '2026-12-31';

-- Year range using EXTRACT
SELECT *
FROM person
WHERE EXTRACT(YEAR FROM dob) BETWEEN 2022 AND 2026;


-- ============================================================
-- 13. LIKE / ILIKE
-- ============================================================

-- Starts with "Bo"
SELECT *
FROM person
WHERE first_name LIKE 'Bo%';

-- Ends with "Bo"
SELECT *
FROM person
WHERE first_name LIKE '%Bo';

-- Contains "Bo"
SELECT *
FROM person
WHERE first_name LIKE '%Bo%';

-- Case-insensitive search
SELECT *
FROM person
WHERE first_name ILIKE '%bo%';

-- Search emails containing amazon
SELECT *
FROM person
WHERE email ILIKE '%amazon%';


-- ============================================================
-- 14. EXISTS
-- ============================================================

-- Check whether at least one person is from India
SELECT EXISTS (
    SELECT 1
    FROM person
    WHERE country = 'India'
);

-- Same idea using SELECT *
SELECT EXISTS (
    SELECT *
    FROM person
    WHERE country = 'India'
);


-- ============================================================
-- 15. GROUP BY
-- ============================================================

-- Count people by country
SELECT country, COUNT(*)
FROM person
GROUP BY country;

-- Count Amazon emails by country
SELECT country,
       COUNT(*) AS amazon_email_count
FROM person
WHERE email ILIKE '%amazon%'
GROUP BY country;


-- ============================================================
-- 16. FILTER WITH AGGREGATES
-- ============================================================

-- Show every country and count Amazon emails
SELECT country,
       COUNT(*) FILTER (
           WHERE email ILIKE '%amazon%'
       ) AS amazon_email_count
FROM person
GROUP BY country
ORDER BY country;


-- ============================================================
-- 17. HAVING
-- ============================================================

-- Countries having more than 10 people
SELECT country,
       COUNT(*) AS people_count
FROM person
GROUP BY country
HAVING COUNT(*) > 10;

-- Countries having at least 2 Amazon emails
SELECT country,
       COUNT(*) FILTER (
           WHERE email ILIKE '%amazon%'
       ) AS amazon_count
FROM person
GROUP BY country
HAVING COUNT(*) FILTER (
    WHERE email ILIKE '%amazon%'
) >= 2;


-- ============================================================
-- 18. AGGREGATE FUNCTIONS
-- ============================================================

-- Count rows
SELECT COUNT(*)
FROM person;

-- Minimum value
SELECT MIN(id)
FROM person;

-- Maximum value
SELECT MAX(id)
FROM person;

-- Average value
SELECT AVG(id)
FROM person;

-- Sum
SELECT SUM(id)
FROM person;


-- ============================================================
-- 19. CAR TABLE
-- ============================================================

CREATE TABLE car (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    make VARCHAR(100) NOT NULL,
    model VARCHAR(100) NOT NULL,
    price NUMERIC(19,2) NOT NULL,
    model_year INT NOT NULL
);


-- ============================================================
-- 20. CAR DATA QUERIES
-- ============================================================

-- View all cars
SELECT *
FROM car;

-- Select specific columns
SELECT make, model, price
FROM car;

-- Sort cars by price
SELECT *
FROM car
ORDER BY price DESC;

-- Most expensive car
SELECT *
FROM car
ORDER BY price DESC
LIMIT 1;

-- Maximum car price
SELECT MAX(price)
FROM car;

-- Average car price
SELECT AVG(price)
FROM car;

-- Minimum car price
SELECT MIN(price)
FROM car;


-- ============================================================
-- 21. MOST EXPENSIVE CAR
-- ============================================================

-- Get complete details of the most expensive car
SELECT *
FROM car
WHERE price = (
    SELECT MAX(price)
    FROM car
);


-- ============================================================
-- 22. GROUP BY WITH CAR DATA
-- ============================================================

-- Average price by make
SELECT make,
       AVG(price) AS avg_price
FROM car
GROUP BY make;

-- Average price by make and model
SELECT make,
       model,
       AVG(price)
FROM car
GROUP BY make, model
ORDER BY make;


-- ============================================================
-- 23. ROUND
-- ============================================================

-- Round average price to 2 decimal places
SELECT make,
       ROUND(AVG(price), 2) AS avg_price
FROM car
GROUP BY make;


-- ============================================================
-- 24. ARITHMETIC
-- ============================================================

-- Arithmetic operators
SELECT
    price,
    price + 100,
    price - 100,
    price * 2,
    price / 2
FROM car;


-- ============================================================
-- 25. PSQL COMMANDS USED
-- ============================================================

-- Connect to another database
-- \c test

-- Quit psql
-- \q

-- Clear query buffer
-- \r

-- Show current query buffer
-- \p

-- Execute query buffer
-- \g

-- Clear Windows terminal
-- \! cls

-- Show psql help
-- \?

-- Show SQL command help
-- \h SELECT

-- Import an SQL file
-- \i 'C:/Users/divya/Downloads/car.sql'

-- Export query output
-- \o filename.txt


-- ============================================================
-- END OF CURRENT SQL PRACTICE
-- ============================================================