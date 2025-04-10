CREATE DATABASE ORDERMANAGEMENT;

USE ORDERMANAGEMENT;


CREATE TABLE Products (
    productId INT PRIMARY KEY,
    productName VARCHAR(100),
    description TEXT,
    price FLOAT,
    quantityInStock INT,
    type VARCHAR(50) CHECK (type IN ('Electronics', 'Clothing'))
);

CREATE TABLE Electronics (
    productId INT PRIMARY KEY,
    brand VARCHAR(100),
    warrantyPeriod INT,
    FOREIGN KEY (productId) REFERENCES Products(productId)
);

CREATE TABLE Clothing (
    productId INT PRIMARY KEY,
    size VARCHAR(10),
    color VARCHAR(50),
    FOREIGN KEY (productId) REFERENCES Products(productId)
);

CREATE TABLE Users (
    userId INT PRIMARY KEY,
    username VARCHAR(100) UNIQUE,
    password VARCHAR(100),
    role VARCHAR(10) CHECK (role IN ('Admin', 'User'))
);

CREATE TABLE Orders (
    orderId INT PRIMARY KEY IDENTITY(1,1),
    userId INT,
    orderDate DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (userId) REFERENCES Users(userId)
);

CREATE TABLE OrderItems (
    orderItemId INT PRIMARY KEY IDENTITY(1,1),
    orderId INT,
    productId INT,
    quantity INT,
    FOREIGN KEY (orderId) REFERENCES Orders(orderId),
    FOREIGN KEY (productId) REFERENCES Products(productId)
);


SELECT * FROM Products;
SELECT * FROM Electronics;
SELECT * FROM Clothing;
SELECT * FROM Users;
SELECT * FROM Orders;
SELECT * FROM OrderItems;







