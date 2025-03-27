--create database today;

--CREATE TABLE Employees (
--    EmpID INT PRIMARY KEY,
--    EmpName VARCHAR(50) NOT NULL,
--    Salary DECIMAL(10,2) CHECK (Salary >= 3000)
--);
--TASK 1
--SELECT 
--    ccu.TABLE_NAME, 
--    ccu.COLUMN_NAME, 
--    cc.CONSTRAINT_NAME, 
--    cc.CHECK_CLAUSE
--FROM 
--    INFORMATION_SCHEMA.CHECK_CONSTRAINTS cc
--JOIN 
--    INFORMATION_SCHEMA.CONSTRAINT_COLUMN_USAGE ccu
--ON 
--    cc.CONSTRAINT_NAME = ccu.CONSTRAINT_NAME
--WHERE 
--    ccu.TABLE_NAME = 'Employees';

--TASK 2

--CREATE TABLE Customers (
--    CustID INT IDENTITY(1,1) PRIMARY KEY,
--    CustName VARCHAR(50),
--    City VARCHAR(50)
--);

--INSERT INTO Customers (CustName, City) VALUES ('John Doe', 'New York');
--INSERT INTO Customers (CustName, City) VALUES ('John Doe', 'New York');

--UPDATE Customers 
--SET City = 'Los Angeles'
--WHERE CustID = (SELECT MIN(CustID) FROM Customers WHERE CustName = 'John Doe' AND City = 'New York');

--TASK 3

--CREATE TABLE Products (
--    ProductID INT PRIMARY KEY,
--    ProductName VARCHAR(50),
--    Price DECIMAL(10,2)
--);

--ALTER TABLE Products 
--ALTER COLUMN ProductName VARCHAR(50) NOT NULL;

--ALTER TABLE Products 
--ADD CONSTRAINT chk_price CHECK (Price > 0);
