--create database joins;
 
 --use joins;

 --Task 1
 --create table salesman(
	--salesman_id INT PRIMARY KEY,
	--name VARCHAR(20),
	--city VARCHAR(20),
	--commission DECIMAL(4,2));

--INSERT INTO salesman VALUES(5001, 'James Hoog', 'New York', 0.15);
--INSERT INTO salesman VALUES(5002, 'Nail Knite ', 'Paris', 0.13);
--INSERT INTO salesman VALUES (5005, 'Pit Alex', 'London', 0.11);
--INSERT INTO salesman VALUES (5006, 'Mc Lyon', 'Paris', 0.14);
--INSERT INTO salesman VALUES (5007, 'Paul Adam', 'Rome', 0.13);
--INSERT INTO salesman VALUES (5003, 'Lauson Hen', 'San Jose', 0.12);

--CREATE TABLE customer(
--	customer_id INT PRIMARY KEY,
--	cust_name VARCHAR(50),
--    city VARCHAR(50),
--    grade INT,
--    salesman_id INT,
--    FOREIGN KEY (salesman_id) REFERENCES salesman(salesman_id)
--);

--INSERT INTO customer VALUES (3002, 'Nick Rimando', 'New York', 100, 5001);
--INSERT INTO customer VALUES (3007, 'Brad Davis', 'New York', 200, 5001);
--INSERT INTO customer VALUES (3005, 'Graham Zusi', 'California', 200, 5002);
--INSERT INTO customer VALUES (3008, 'Julian Green', 'London', 300, 5002);
--INSERT INTO customer VALUES (3004, 'Fabian Johnson', 'Paris', 300, 5006);
--INSERT INTO customer VALUES (3009, 'Geoff Cameron', 'Berlin', 100, 5003);
--INSERT INTO customer VALUES (3003, 'Jozy Altidor', 'Moscow', 200, 5007);
--INSERT INTO customer VALUES (3001, 'Brad Guzan', 'London', NULL, 5005);

--SELECT s.name as Salesman, c.cust_name, s.city 
--FROM salesman s JOIN customer c
--on s.city=c.city;

--Task 2
--CREATE TABLE orders (
--    ord_no INT PRIMARY KEY,
--    purch_amt DECIMAL(10,2),
--    ord_date DATE,
--    customer_id INT,
--    salesman_id INT,
--    FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
--    FOREIGN KEY (salesman_id) REFERENCES salesman(salesman_id)
--);

--INSERT INTO orders VALUES (70001, 150.5, '2012-10-05', 3005, 5002);
--INSERT INTO orders VALUES (70009, 270.65, '2012-09-10', 3001, 5005);
--INSERT INTO orders VALUES (70002, 65.26, '2012-10-05', 3002, 5001);
--INSERT INTO orders VALUES (70004, 110.5, '2012-08-17', 3009, 5003);
--INSERT INTO orders VALUES (70007, 948.5, '2012-09-10', 3005, 5002);
--INSERT INTO orders VALUES (70005, 2400.6, '2012-07-27', 3007, 5001);
--INSERT INTO orders VALUES (70008, 5760, '2012-09-10', 3002, 5001);
--INSERT INTO orders VALUES (70010, 1983.43, '2012-10-10', 3004, 5006);
--INSERT INTO orders VALUES (70003, 2480.4, '2012-10-10', 3009, 5003);

--SELECT o.ord_no, o.purch_amt, c.cust_name, c.city 
--FROM customer c
--JOIN orders o ON c.customer_id=o.customer_id
--WHERE purch_amt>500 AND purch_amt<2000;

--Task 3
--SELECT c.cust_name AS Customer, c.city, s.name AS Salesman, s.commission
--FROM customer c
--JOIN salesman s ON c.salesman_id = s.salesman_id;

--Task 4
--SELECT c.cust_name AS Customer, c.city, s.name AS Salesman, s.commission
--FROM customer c
--JOIN salesman s ON c.salesman_id = s.salesman_id 
--WHERE s.commission > 0.12;

--Task 5
--SELECT c.cust_name AS Customer, c.city AS Customer_City, 
--       s.name AS Salesman, s.city AS Salesman_City, s.commission
--FROM customer c
--JOIN salesman s ON c.salesman_id = s.salesman_id
--WHERE c.city <> s.city AND s.commission > 0.12;

--Task 6
--SELECT o.ord_no, o.ord_date, o.purch_amt, 
--       c.cust_name AS Customer, c.grade, 
--       s.name AS Salesman, s.commission
--FROM orders o
--JOIN customer c ON o.customer_id = c.customer_id
--JOIN salesman s ON o.salesman_id = s.salesman_id;

--Task 7
--SELECT o.ord_no, o.ord_date, o.purch_amt, 
--       c.cust_name AS Customer, c.city AS Customer_City, c.grade,
--       s.name AS Salesman, s.city AS Salesman_City, s.commission
--FROM orders o
--JOIN customer c ON o.customer_id = c.customer_id
--JOIN salesman s ON o.salesman_id = s.salesman_id;

--Task 7
--SELECT c.cust_name AS Customer, c.city AS Customer_City, c.grade, 
--       s.name AS Salesman, s.city AS Salesman_City
--FROM customer c
--JOIN salesman s ON c.salesman_id = s.salesman_id
--ORDER BY c.customer_id ASC;

--Task 8
--SELECT c.cust_name AS Customer, c.city AS Customer_City, c.grade, 
--       s.name AS Salesman, s.city AS Salesman_City
--FROM customer c
--JOIN salesman s ON c.salesman_id = s.salesman_id
--ORDER BY c.customer_id ASC;

--Task 9
--SELECT c.cust_name AS Customer, c.city AS Customer_City, c.grade, 
--       s.name AS Salesman, s.city AS Salesman_City
--FROM customer c
--JOIN salesman s ON c.salesman_id = s.salesman_id
--WHERE c.grade < 300
--ORDER BY c.customer_id ASC;

--Task 10
--SELECT c.cust_name AS Customer, c.city AS Customer_City, 
--       o.ord_no, o.ord_date, o.purch_amt
--FROM customer c
--LEFT JOIN orders o ON c.customer_id = o.customer_id
--ORDER BY o.ord_date ASC;

--Task 11
--SELECT 
--    c.cust_name, 
--    c.city, 
--    o.ord_no, 
--    o.ord_date, 
--    o.purch_amt, 
--    s.name AS salesman_name, 
--    s.commission
--FROM customer c
--LEFT JOIN orders o ON c.customer_id = o.customer_id
--LEFT JOIN salesman s ON c.salesman_id = s.salesman_id
--ORDER BY c.cust_name;

--Task 12
--SELECT DISTINCT s.salesman_id, s.name, s.city, s.commission
--FROM salesman s
--LEFT JOIN customer c ON s.salesman_id = c.salesman_id
--ORDER BY s.name;

--Task 13
--SELECT 
--    s.salesman_id, 
--    s.name AS salesman_name, 
--    c.cust_name, 
--    c.city AS customer_city, 
--    c.grade, 
--    o.ord_no, 
--    o.ord_date, 
--    o.purch_amt
--FROM salesman s
--LEFT JOIN customer c ON s.salesman_id = c.salesman_id
--LEFT JOIN orders o ON c.customer_id = o.customer_id
--ORDER BY s.name, c.cust_name;

--Task 14
--SELECT DISTINCT s.salesman_id, s.name, s.city, s.commission
--FROM salesman s
--LEFT JOIN customer c ON s.salesman_id = c.salesman_id
--LEFT JOIN orders o ON c.customer_id = o.customer_id
--WHERE (o.purch_amt >= 2000 AND c.grade IS NOT NULL) OR o.customer_id IS NULL
--ORDER BY s.name;

--Task 15
--SELECT c.cust_name AS Customer, c.city, o.ord_no, o.ord_date, o.purch_amt
--FROM orders o
--LEFT JOIN customer c
--ON c.customer_id=o.customer_id
--ORDER BY c.cust_name,o.ord_no;

--Task 16
--SELECT 
--    c.cust_name AS cust_name, 
--    c.city AS city, 
--    o.ord_no, 
--    o.ord_date, 
--    o.purch_amt
--FROM orders o
--LEFT JOIN customer c ON o.customer_id = c.customer_id
--WHERE 
--    (c.grade IS NOT NULL AND o.customer_id IS NOT NULL) 
--    OR (c.customer_id IS NULL);

--Task 17
--SELECT 
--    s.salesman_id, 
--    s.name AS salesman_name, 
--    s.city AS salesman_city, 
--    s.commission, 
--    c.customer_id, 
--    c.cust_name, 
--    c.city AS customer_city, 
--    c.grade, 
--    c.salesman_id AS assigned_salesman_id
--FROM salesman s
--CROSS JOIN customer c;


--Task 18
--SELECT 
--    s.salesman_id, 
--    s.name AS salesman_name, 
--    s.city AS salesman_city, 
--    s.commission, 
--    c.customer_id, 
--    c.cust_name AS customer_name, 
--    c.city AS customer_city, 
--    c.grade
--FROM salesman s
--CROSS JOIN customer c
--WHERE s.city = c.city;


--Task 19
--SELECT 
--    s.salesman_id, 
--    s.name AS salesman_name, 
--    s.city AS salesman_city, 
--    s.commission, 
--    c.customer_id, 
--    c.cust_name AS customer_name, 
--    c.city AS customer_city, 
--    c.grade
--FROM salesman s
--CROSS JOIN customer c
--WHERE s.city IS NOT NULL 
--AND c.grade IS NOT NULL;


--Task 20
--SELECT 
--    s.salesman_id, 
--    s.name AS salesman_name, 
--    s.city AS salesman_city, 
--    s.commission, 
--    c.customer_id, 
--    c.cust_name AS customer_name, 
--    c.city AS customer_city, 
--    c.grade
--FROM salesman s
--CROSS JOIN customer c
--WHERE s.city <> c.city 
--AND c.grade IS NOT NULL;



--Task 21
--CREATE TABLE company_mast (
--    COM_ID INT PRIMARY KEY,
--    COM_NAME VARCHAR(50)
--);	

--INSERT INTO company_mast (COM_ID, COM_NAME) VALUES
--(11, 'Samsung'),
--(12, 'iBall'),
--(13, 'Epsion'),
--(14, 'Zebronics'),
--(15, 'Asus'),
--(16, 'Frontech');

--CREATE TABLE item_mast (
--    PRO_ID INT PRIMARY KEY,
--    PRO_NAME VARCHAR(50),
--    PRO_PRICE DECIMAL(10,2),
--    PRO_COM INT,
--    FOREIGN KEY (PRO_COM) REFERENCES company_mast(COM_ID)
--);

--INSERT INTO item_mast (PRO_ID, PRO_NAME, PRO_PRICE, PRO_COM) VALUES
--(101, 'Mother Board', 3200.00, 15),
--(102, 'Key Board', 450.00, 16),
--(103, 'ZIP drive', 250.00, 14),
--(104, 'Speaker', 550.00, 16),
--(105, 'Monitor', 5000.00, 11),
--(106, 'DVD drive', 900.00, 12),
--(107, 'CD drive', 800.00, 12),
--(108, 'Printer', 2600.00, 13),
--(109, 'Refill cartridge', 350.00, 13),
--(110, 'Mouse', 250.00, 12);

--SELECT 
--    i.PRO_ID, 
--    i.PRO_NAME, 
--    i.PRO_PRICE, 
--    c.COM_ID, 
--    c.COM_NAME
--FROM item_mast i
--INNER JOIN company_mast c 
--ON i.PRO_COM = c.COM_ID;


--Task 22
--SELECT 
--    i.PRO_NAME, 
--    i.PRO_PRICE, 
--    c.COM_NAME
--FROM item_mast i
--INNER JOIN company_mast c 
--ON i.PRO_COM = c.COM_ID;


--Task 23
--SELECT 
--    c.COM_NAME, 
--    AVG(i.PRO_PRICE) AS AVG_PRICE
--FROM item_mast i
--INNER JOIN company_mast c 
--ON i.PRO_COM = c.COM_ID
--GROUP BY c.COM_NAME;


--Task 24
--SELECT 
--    c.COM_NAME, 
--    AVG(i.PRO_PRICE) AS AVG_PRICE
--FROM item_mast i
--INNER JOIN company_mast c 
--ON i.PRO_COM = c.COM_ID
--GROUP BY c.COM_NAME
--HAVING AVG(i.PRO_PRICE) >= 350;


--Task 25
--SELECT 
--    i.PRO_NAME, 
--    i.PRO_PRICE, 
--    c.COM_NAME
--FROM item_mast i
--INNER JOIN company_mast c 
--ON i.PRO_COM = c.COM_ID
--WHERE i.PRO_PRICE = (
--    SELECT MAX(PRO_PRICE) 
--    FROM item_mast 
--    WHERE PRO_COM = i.PRO_COM
--);


--Task 26
--CREATE TABLE emp_department (
--    DPT_CODE INT PRIMARY KEY,
--    DPT_NAME VARCHAR(50),
--    DPT_ALLOTMENT DECIMAL(10,2)
--);

--INSERT INTO emp_department (DPT_CODE, DPT_NAME, DPT_ALLOTMENT) VALUES
--(57, 'IT', 65000),
--(63, 'Finance', 15000),
--(47, 'HR', 240000),
--(27, 'RD', 55000),
--(89, 'QC', 75000);

--CREATE TABLE emp_details (
--    EMP_IDNO INT PRIMARY KEY,
--    EMP_FNAME VARCHAR(50),
--    EMP_LNAME VARCHAR(50),
--    EMP_DEPT INT,
--    FOREIGN KEY (EMP_DEPT) REFERENCES emp_department(DPT_CODE)
--);

--INSERT INTO emp_details (EMP_IDNO, EMP_FNAME, EMP_LNAME, EMP_DEPT) VALUES
--(127323, 'Michale', 'Robbin', 57),
--(526689, 'Carlos', 'Snares', 63),
--(843795, 'Enric', 'Dosio', 57),
--(328717, 'Jhon', 'Snares', 63),
--(444527, 'Joseph', 'Dosni', 47),
--(659831, 'Zanifer', 'Emily', 47),
--(847674, 'Kuleswar', 'Sitaraman', 57),
--(748681, 'Henrey', 'Gabriel', 47),
--(555935, 'Alex', 'Manuel', 57);

--SELECT 
--    e.EMP_IDNO, 
--    e.EMP_FNAME, 
--    e.EMP_LNAME, 
--    e.EMP_DEPT, 
--    d.DPT_NAME, 
--    d.DPT_ALLOTMENT
--FROM emp_details e
--INNER JOIN emp_department d 
--ON e.EMP_DEPT = d.DPT_CODE;


--Task 27
--SELECT 
--    e.EMP_FNAME, 
--    e.EMP_LNAME, 
--    d.DPT_NAME, 
--    d.DPT_ALLOTMENT
--FROM emp_details e
--INNER JOIN emp_department d 
--ON e.EMP_DEPT = d.DPT_CODE;


--Task 28
--SELECT 
--    e.EMP_FNAME, 
--    e.EMP_LNAME
--FROM emp_details e
--INNER JOIN emp_department d 
--ON e.EMP_DEPT = d.DPT_CODE
--WHERE d.DPT_ALLOTMENT > 50000;


--Task 29
--SELECT d.DPT_NAME
--FROM emp_details e
--INNER JOIN emp_department d 
--ON e.EMP_DEPT = d.DPT_CODE
--GROUP BY d.DPT_NAME
--HAVING COUNT(e.EMP_IDNO) > 2;
