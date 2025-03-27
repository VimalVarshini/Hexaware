--create database scenario;
 --use scenario;
 -- Scenario 1
-- CREATE TABLE Employees (
--    EmployeeID INT PRIMARY KEY IDENTITY(1,1),
--    Name VARCHAR(100) NOT NULL,
--    Department VARCHAR(50) NOT NULL,
--    Salary DECIMAL(10,2) NOT NULL
--);

--INSERT INTO Employees (Name, Department, Salary) 
--VALUES 
--('Alice Johnson', 'HR', 60000),
--('Bob Smith', 'IT', 55000),
--('Charlie Brown', 'HR', 48000),
--('David Wilson', 'Finance', 70000),
--('Emma Davis', 'HR', 52000);

--SELECT Name 
--FROM Employees 
--WHERE Department = 'HR' AND Salary > 50000;

-- Scenario 2
--CREATE TABLE Orders (
--    OrderID INT PRIMARY KEY IDENTITY(1,1),
--    CustomerID INT NOT NULL,
--    OrderDate DATE NOT NULL,
--    OrderAmount DECIMAL(10,2) NOT NULL
--);

--INSERT INTO Orders (CustomerID, OrderDate, OrderAmount) 
--VALUES 
--(101, '2025-03-15', 250.00),
--(102, '2025-03-16', 300.00),
--(103, '2025-03-17', 150.00),
--(101, '2025-03-18', 200.00),
--(104, '2025-03-19', 180.00),
--(102, '2025-03-20', 350.00),
--(105, '2025-03-21', 400.00);


--SELECT CustomerID, COUNT(*) AS DuplicateCount 
--FROM Orders 
--GROUP BY CustomerID 
--HAVING COUNT(*) > 1;

-- Scenario 3
--CREATE TABLE Sales (
--    SaleID INT PRIMARY KEY IDENTITY(1,1),
--    ProductID INT NOT NULL,
--    Quantity INT NOT NULL,
--    SaleDate DATE NOT NULL
--);

--INSERT INTO Sales (ProductID, Quantity, SaleDate) 
--VALUES 
--(1, 10, '2025-03-10'),
--(2, 5, '2025-03-11'),
--(1, 8, '2025-03-12'),
--(3, 12, '2025-03-13'),
--(2, 7, '2025-03-14'),
--(1, 6, '2025-03-15'),
--(3, 9, '2025-03-16');

--SELECT ProductID, SUM(Quantity) AS TotalQuantitySold 
--FROM Sales 
--GROUP BY ProductID;

-- Scenario 4
--CREATE TABLE Transactions (
--    TransactionID INT PRIMARY KEY IDENTITY(1,1),
--    AccountID INT NOT NULL,
--    TransactionDate DATE NOT NULL,
--    Amount DECIMAL(10,2) NOT NULL
--);

--INSERT INTO Transactions (AccountID, TransactionDate, Amount) 
--VALUES 
--(1001, '2025-02-15', 500.00),  -- Outside 30-day range
--(1002, '2025-02-28', 300.00),  -- Outside 30-day range
--(1003, '2025-03-01', 200.00),  -- Within 30-day range
--(1004, '2025-03-10', 150.00),  -- Within 30-day range
--(1005, '2025-03-18', 400.00),  -- Within 30-day range
--(1006, '2025-03-20', 250.00);  -- Within 30-day range

--SELECT * 
--FROM Transactions 
--WHERE TransactionDate >= DATEADD(DAY, -30, GETDATE());

-- Scenario 5
--CREATE TABLE Products (
--    ProductID INT PRIMARY KEY IDENTITY(1,1),
--    ProductName VARCHAR(100) NOT NULL,
--    Price DECIMAL(10,2) NOT NULL,
--    StockQuantity INT NOT NULL
--);

--INSERT INTO Products (ProductName, Price, StockQuantity) 
--VALUES 
--('Laptop', 1000.00, 50),   -- Should be updated
--('Mouse', 25.00, 200),     -- Should NOT be updated
--('Keyboard', 45.00, 80),   -- Should be updated
--('Monitor', 300.00, 30),   -- Should be updated
--('Printer', 150.00, 120);  -- Should NOT be updated

--UPDATE Products 
--SET Price = Price * 1.10 
--WHERE StockQuantity < 100;

-- Scenario 6
--CREATE TABLE Users (
--    UserID INT PRIMARY KEY IDENTITY(1,1),
--    Username VARCHAR(50) NOT NULL,
--    Email VARCHAR(100) NOT NULL UNIQUE,
--    Status VARCHAR(20) NOT NULL,
--    LastLogin DATE NULL
--);

--INSERT INTO Users (Username, Email, Status, LastLogin) 
--VALUES 
--('Alice', 'alice@example.com', 'active', '2025-02-15'),   
--('Bob', 'bob@example.com', 'inactive', '2023-12-10'),    
--('Charlie', 'charlie@example.com', 'inactive', '2024-02-20'), 
--('David', 'david@example.com', 'inactive', '2025-03-01'), 
--('Emma', 'emma@example.com', 'active', '2024-11-25');    

--DELETE FROM Users 
--WHERE Status = 'inactive' 
--AND LastLogin < DATEADD(YEAR, -1, GETDATE());

-- Scenario 9
--CREATE TABLE Product (
--    ProductID INT PRIMARY KEY IDENTITY(1,1),
--    ProductName VARCHAR(100) NOT NULL,
--    Category VARCHAR(50),
--    Discount DECIMAL(5,2) NULL
--);

--INSERT INTO Product (ProductName, Category, Discount) 
--VALUES 
--('Laptop', 'Electronics', 10.00),
--('Mouse', 'Accessories', NULL),
--('Keyboard', 'Accessories', 5.00),
--('Monitor', 'Electronics', NULL),
--('Printer', 'Office Supplies', 8.00);

--SELECT ProductName, 
--       COALESCE(CAST(Discount AS VARCHAR), 'No Discount') AS Discount 
--FROM Product;


