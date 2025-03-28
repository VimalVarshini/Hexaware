--Tasks 1: Database Design
--CREATE DATABASE HMBank;

--USE HMBank;

--CREATE TABLE Customers (
--    customer_id INT IDENTITY(1,1) PRIMARY KEY,
--    first_name NVARCHAR(50) NOT NULL,
--    last_name NVARCHAR(50) NOT NULL,
--    DOB DATE NOT NULL,
--    email NVARCHAR(100) UNIQUE NOT NULL,
--    phone_number NVARCHAR(15) UNIQUE NOT NULL,
--    address NVARCHAR(255) NOT NULL
--);

--CREATE TABLE Accounts (
--    account_id INT IDENTITY(1,1) PRIMARY KEY,
--    customer_id INT NOT NULL,
--    account_type NVARCHAR(20) CHECK (account_type IN ('savings', 'current', 'zero_balance')) NOT NULL,
--    balance DECIMAL(18,2) NOT NULL DEFAULT 0.00,
--    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE
--);

--CREATE TABLE Transactions (
--    transaction_id INT IDENTITY(1,1) PRIMARY KEY,
--    account_id INT NOT NULL,
--    transaction_type NVARCHAR(20) CHECK (transaction_type IN ('deposit', 'withdrawal', 'transfer')) NOT NULL,
--    amount DECIMAL(18,2) NOT NULL,
--    transaction_date DATETIME DEFAULT GETDATE(),
--    FOREIGN KEY (account_id) REFERENCES Accounts(account_id) ON DELETE CASCADE
--);

--Tasks 2: Select, Where, Between, AND, LIKE
--Ques 1
--INSERT INTO Customers (first_name, last_name, DOB, email, phone_number, address) VALUES
--('John', 'Doe', '1985-04-12', 'john.doe@example.com', '9876543210', '123 Main Str, NEW YORK'),
--('Jane', 'Smith', '1990-07-19', 'jane.smith@example.com', '8765432109', '456 Oak Str, CANADA'),
--('Robert', 'Brown', '1978-02-23', 'robert.brown@example.com', '7654321098', '78 Bala Str, INDIA');

--INSERT INTO Accounts (customer_id, account_type, balance) VALUES
--(1, 'savings', 5000.00),
--(2, 'current', 1500.00),
--(3, 'savings', 3000.00),
--(1, 'current', 2500.00),
--(2, 'savings', 1000.00);

--INSERT INTO Transactions (account_id, transaction_type, amount) VALUES
--(1, 'deposit', 1000.00),
--(2, 'withdrawal', 500.00),
--(3, 'deposit', 2000.00),
--(4, 'transfer', 750.00),
--(5, 'withdrawal', 300.00);

--Ques 2
--1
--SELECT CONCAT(first_name, ' ', last_name) AS full_name, account_type, email
--FROM Customers
--JOIN Accounts ON Customers.customer_id = Accounts.customer_id;

--2
--SELECT Customers.first_name, Customers.last_name, Transactions.*
--FROM Customers
--JOIN Accounts ON Customers.customer_id = Accounts.customer_id
--JOIN Transactions ON Accounts.account_id = Transactions.account_id;

--3
--UPDATE Accounts 
--SET balance = balance + 500 
--WHERE account_id = 1;

--4
--SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM Customers;

--5
--DELETE FROM Accounts 
--WHERE balance = 0 AND account_type = 'savings';

--6
--SELECT * FROM Customers 
--WHERE address LIKE '%NEW YORK%';

--7
--SELECT balance FROM Accounts WHERE account_id = 2;

--8
--SELECT * FROM Accounts 
--WHERE account_type = 'current' AND balance > 1000;

--9
--SELECT * FROM Transactions 
--WHERE account_id = 3;

--10
--SELECT account_id, balance, balance * 0.05 AS interest 
--FROM Accounts 
--WHERE account_type = 'savings';

--11
--SELECT * FROM Accounts 
--WHERE balance < 500;

--12
--SELECT * FROM Customers 
--WHERE address NOT LIKE '%NEW YORK%';

--Tasks 3: Aggregate functions, Having, Order By, GroupBy and Joins
--Ques 1
--SELECT AVG(balance) AS avg_balance FROM Accounts;

--Ques 2
--SELECT TOP 10 * FROM Accounts 
--ORDER BY balance DESC;

--Ques 3
--SELECT SUM(amount) AS total_deposits 
--FROM Transactions 
--WHERE transaction_type = 'deposit' 
--AND CAST(transaction_date AS DATE) = '2024-03-01';

--Ques 4
--SELECT TOP 1 * FROM Customers 
--ORDER BY DOB ASC;

--SELECT TOP 1 * FROM Customers 
--ORDER BY DOB DESC;

--Ques 5
--SELECT Transactions.*, Accounts.account_type 
--FROM Transactions 
--JOIN Accounts ON Transactions.account_id = Accounts.account_id;

--Ques 6
--SELECT Customers.*, Accounts.account_id, Accounts.account_type, Accounts.balance 
--FROM Customers 
--JOIN Accounts ON Customers.customer_id = Accounts.customer_id;

--Ques 7
--SELECT Transactions.*, Customers.first_name, Customers.last_name 
--FROM Transactions 
--JOIN Accounts ON Transactions.account_id = Accounts.account_id
--JOIN Customers ON Accounts.customer_id = Customers.customer_id
--WHERE Transactions.account_id = 2;

--Ques 8
--SELECT customer_id, COUNT(*) AS account_count 
--FROM Accounts 
--GROUP BY customer_id 
--HAVING COUNT(*) > 1;

--Ques 9
--SELECT 
--    SUM(CASE WHEN transaction_type = 'deposit' THEN amount ELSE 0 END) -
--    SUM(CASE WHEN transaction_type = 'withdrawal' THEN amount ELSE 0 END) AS net_difference
--FROM Transactions;

--Ques 10
--SELECT account_id, AVG(balance) AS avg_daily_balance 
--FROM Accounts 
--GROUP BY account_id;

--Ques 11
--SELECT account_type, SUM(balance) AS total_balance 
--FROM Accounts 
--GROUP BY account_type;

--Ques 12
--SELECT account_id, COUNT(*) AS transaction_count 
--FROM Transactions 
--GROUP BY account_id 
--ORDER BY transaction_count DESC;

--Ques 13
--SELECT Customers.customer_id, Customers.first_name, Customers.last_name, 
--       Accounts.account_type, COALESCE(SUM(Accounts.balance), 0) AS total_balance
--FROM Customers
--JOIN Accounts ON Customers.customer_id = Accounts.customer_id
--GROUP BY Customers.customer_id, Customers.first_name, Customers.last_name, Accounts.account_type
--HAVING COALESCE(SUM(Accounts.balance), 0) > 5000;

--Ques 14
--SELECT account_id, ROUND(amount, 2) AS amount, CAST(transaction_date AS DATE) AS transaction_date, COUNT(*) AS duplicate_count
--FROM Transactions
--GROUP BY account_id, ROUND(amount, 2), CAST(transaction_date AS DATE)
--HAVING COUNT(*) > 1;

--Tasks 4: Subquery
--Ques 1
--SELECT C.customer_id, C.first_name, C.last_name, A.balance
--FROM Customers C
--JOIN Accounts A ON C.customer_id = A.customer_id
--WHERE A.balance = (SELECT MAX(balance) FROM Accounts);

--Ques 2
--SELECT AVG(balance) AS avg_balance
--FROM Accounts
--WHERE customer_id IN (
--    SELECT customer_id 
--    FROM Accounts 
--    GROUP BY customer_id 
--    HAVING COUNT(*) > 1
--);

--Ques 3
--SELECT *
--FROM Transactions
--WHERE amount > (SELECT AVG(amount) FROM Transactions);

--Ques 4
--SELECT C.customer_id, C.first_name, C.last_name
--FROM Customers C
--LEFT JOIN Accounts A ON C.customer_id = A.customer_id
--LEFT JOIN Transactions T ON A.account_id = T.account_id
--WHERE T.transaction_id IS NULL;

--Ques 5
--SELECT SUM(A.balance) AS total_balance
--FROM Accounts A
--WHERE A.account_id NOT IN (SELECT DISTINCT account_id FROM Transactions);

--Ques 6
--SELECT *
--FROM Transactions
--WHERE account_id IN (
--    SELECT account_id 
--    FROM Accounts 
--    WHERE balance = (SELECT MIN(balance) FROM Accounts)
--);

--Ques 7
--SELECT customer_id
--FROM Accounts
--GROUP BY customer_id
--HAVING COUNT(DISTINCT account_type) > 1;

--Ques 8
--SELECT account_type, 
--       COUNT(*) AS type_count,
--       (COUNT(*) * 100.0) / (SELECT COUNT(*) FROM Accounts) AS percentage
--FROM Accounts
--GROUP BY account_type;

--Ques 9
--SELECT T.*
--FROM Transactions T
--JOIN Accounts A ON T.account_id = A.account_id
--WHERE A.customer_id = 1; -- Replace with actual customer_id


--Ques 10
--SELECT account_type, 
--       (SELECT SUM(balance) FROM Accounts A2 WHERE A1.account_type = A2.account_type) AS total_balance
--FROM Accounts A1
--GROUP BY account_type;
