--Create the database
CREATE DATABASE Banking;

USE Banking;


--Customers Table
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY IDENTITY(1,1),
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    DOB DATE,
    email VARCHAR(100),
    phone_number VARCHAR(15),
    address VARCHAR(255)
);

--Accounts Table
CREATE TABLE Accounts (
    account_id INT PRIMARY KEY IDENTITY(1001,1),
    customer_id INT,
    account_type VARCHAR(20),
    balance DECIMAL(15,2),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

--Transactions Table
CREATE TABLE Transactions (
    transaction_id INT PRIMARY KEY IDENTITY(1,1),
    account_id INT,
    transaction_type VARCHAR(20),
    amount DECIMAL(15,2),
    transaction_date DATETIME DEFAULT GETDATE(),
    description VARCHAR(255), 
    FOREIGN KEY (account_id) REFERENCES Accounts(account_id)
);

SELECT * FROM Customers;
SELECT * FROM Accounts;
SELECT * FROM Transactions;