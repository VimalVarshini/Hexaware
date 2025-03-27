--CREATE DATABASE EcommerceDB;

--USE EcommerceDB;

--CREATE TABLE customers (
--    customer_id INT PRIMARY KEY,
--    first_name VARCHAR(50),
--    last_name VARCHAR(50),
--    email VARCHAR(100),
--    address VARCHAR(255)
--);

--INSERT INTO customers (customer_id, first_name, last_name, email, address) VALUES
--(1, 'John', 'Doe', 'johndoe@example.com', '123 Main St, City'),
--(2, 'Jane', 'Smith', 'janesmith@example.com', '456 Elm St, Town'),
--(3, 'Robert', 'Johnson', 'robert@example.com', '789 Oak St, Village'),
--(4, 'Sarah', 'Brown', 'sarah@example.com', '101 Pine St, Suburb'),
--(5, 'David', 'Lee', 'david@example.com', '234 Cedar St, District'),
--(6, 'Laura', 'Hall', 'laura@example.com', '567 Birch St, County'),
--(7, 'Michael', 'Davis', 'michael@example.com', '890 Maple St, State'),
--(8, 'Emma', 'Wilson', 'emma@example.com', '321 Redwood St, Country'),
--(9, 'William', 'Taylor', 'william@example.com', '432 Spruce St, Province'),
--(10, 'Olivia', 'Adams', 'olivia@example.com', '765 Fir St, Territory');

--CREATE TABLE products (
--    product_id INT PRIMARY KEY,
--    name VARCHAR(100),
--    description TEXT,
--    price DECIMAL(10,2),
--    stock_quantity INT
--);

--INSERT INTO products (product_id, name, description, price, stock_quantity) VALUES
--(1, 'Laptop', 'High-performance laptop', 800.00, 10),
--(2, 'Smartphone', 'Latest smartphone', 600.00, 15),
--(3, 'Tablet', 'Portable tablet', 300.00, 20),
--(4, 'Headphones', 'Noise-canceling', 150.00, 30),
--(5, 'TV', '4K Smart TV', 900.00, 5),
--(6, 'Coffee Maker', 'Automatic coffee maker', 50.00, 25),
--(7, 'Refrigerator', 'Energy-efficient', 700.00, 10),
--(8, 'Microwave Oven', 'Countertop microwave', 80.00, 15),
--(9, 'Blender', 'High-speed blender', 70.00, 20),
--(10, 'Vacuum Cleaner', 'Bagless vacuum cleaner', 120.00, 10);

--CREATE TABLE cart (
--    cart_id INT PRIMARY KEY,
--    customer_id INT,
--    product_id INT,
--    quantity INT,
--    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
--    FOREIGN KEY (product_id) REFERENCES products(product_id)
--);

--INSERT INTO cart (cart_id, customer_id, product_id, quantity) VALUES
--(1, 1, 1, 2),
--(2, 1, 3, 1),
--(3, 2, 2, 3),
--(4, 3, 4, 4),
--(5, 3, 5, 2),
--(6, 4, 6, 1),
--(7, 5, 1, 1),
--(8, 6, 10, 2),
--(9, 6, 9, 3),
--(10, 7, 7, 2);


--CREATE TABLE orders (
--    order_id INT PRIMARY KEY,
--    customer_id INT,
--    order_date DATE,
--    total_price DECIMAL(10,2),
--    shipping_address VARCHAR(255),
--    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
--);

--INSERT INTO orders (order_id, customer_id, order_date, total_price, shipping_address) VALUES
--(1, 1, '2023-01-05', 1200.00, '123 Main St, City'),
--(2, 2, '2023-02-10', 900.00, '456 Elm St, Town'),
--(3, 3, '2023-03-15', 300.00, '789 Oak St, Village'),
--(4, 4, '2023-04-20', 150.00, '101 Pine St, Suburb'),
--(5, 5, '2023-05-25', 1800.00, '234 Cedar St, District'),
--(6, 6, '2023-06-30', 400.00, '567 Birch St, County'),
--(7, 7, '2023-07-05', 700.00, '890 Maple St, State'),
--(8, 8, '2023-08-10', 160.00, '321 Redwood St, Country'),
--(9, 9, '2023-09-15', 140.00, '432 Spruce St, Province'),
--(10, 10, '2023-10-20', 1400.00, '765 Fir St, Territory');

--CREATE TABLE order_items (
--    order_item_id INT PRIMARY KEY,
--    order_id INT,
--    product_id INT,
--    quantity INT,
--    item_amount DECIMAL(10,2),
--    FOREIGN KEY (order_id) REFERENCES orders(order_id),
--    FOREIGN KEY (product_id) REFERENCES products(product_id)
--);

--INSERT INTO order_items (order_item_id, order_id, product_id, quantity, item_amount) VALUES
--(1, 1, 1, 2, 1600.00),
--(2, 1, 3, 1, 300.00),
--(3, 2, 2, 3, 1800.00),
--(4, 3, 5, 2, 1800.00),
--(5, 4, 4, 4, 600.00),
--(6, 4, 6, 1, 50.00),
--(7, 5, 1, 1, 800.00),
--(8, 5, 2, 2, 1200.00),
--(9, 6, 10, 2, 240.00),
--(10, 6, 9, 3, 210.00);

--Ques 1
--UPDATE products
--SET price = 800
--WHERE name = 'Refrigerator';

--Ques 2
--DELETE FROM cart
--WHERE customer_id = 5;

--Ques 3
--SELECT * FROM products
--WHERE price < 100;

--Ques 4
--SELECT * FROM products
--WHERE stock_quantity > 5;

--Ques 5
--SELECT * FROM orders
--WHERE total_price BETWEEN 500 AND 1000;

--Ques 6
--SELECT * FROM products
--WHERE name LIKE '%r';

--Ques 7
--SELECT * FROM cart
--WHERE customer_id = 5;

--Ques 8
--SELECT DISTINCT customers.*
--FROM customers
--JOIN orders ON customers.customer_id = orders.customer_id
--WHERE order_date BETWEEN '2023-01-01' AND '2023-12-31';

--Ques 9
--SELECT name, MIN(stock_quantity) AS min_stock
--FROM products
--GROUP BY name;

--Ques 10
--SELECT customers.customer_id, customers.first_name, SUM(orders.total_price) AS total_spent
--FROM customers
--JOIN orders ON customers.customer_id = orders.customer_id
--GROUP BY customers.customer_id, customers.first_name;

--Ques 11
--SELECT customer_id, AVG(total_price) AS avg_order_amount
--FROM orders
--GROUP BY customer_id;

--Ques 12
--SELECT customer_id, COUNT(*) AS order_count
--FROM orders
--GROUP BY customer_id;

--Ques 13
--SELECT customer_id, MAX(total_price) AS max_order_amount
--FROM orders
--GROUP BY customer_id;

--Ques 14
--SELECT customer_id, SUM(total_price) AS total_spent
--FROM orders
--GROUP BY customer_id
--HAVING SUM(total_price) > 1000;

--Ques 15
--SELECT * FROM products
--WHERE product_id NOT IN (SELECT DISTINCT product_id FROM cart);

--Ques 16
--SELECT * 
--FROM customers c
--WHERE NOT EXISTS (
--    SELECT 1 FROM orders o WHERE o.customer_id = c.customer_id
--);


--Ques 17
--SELECT product_id, 
--       (SUM(item_amount) * 100 / (SELECT SUM(total_price) FROM orders)) AS revenue_percentage
--FROM order_items
--GROUP BY product_id;

--Ques 18
--SELECT * FROM products
--WHERE stock_quantity < 5;

--Ques 19
--SELECT DISTINCT customer_id
--FROM orders
--WHERE total_price > 1000;
