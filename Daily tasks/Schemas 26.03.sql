--Task 1

--CREATE DATABASE source_db;

--USE source_db;

--CREATE TABLE dbo.customer (
--    id INT PRIMARY KEY,
--    name VARCHAR(50),
--    email VARCHAR(100)
--);

--INSERT INTO dbo.customer (id, name, email) VALUES
--(1, 'John Doe', 'john@example.com'),
--(2, 'Jane Doe', 'jane@example.com');

--SELECT * FROM dbo.customer;

--CREATE DATABASE target_db;

--USE target_db;

--SELECT * INTO target_db.dbo.customer FROM source_db.dbo.customer;

--USE target_db;
--SELECT * FROM dbo.customer;

--Task 2

--USE source_db;

--CREATE SCHEMA my_schema_old;

--CREATE SCHEMA my_schema_new;

--CREATE TABLE my_schema_old.emp (
--    id INT PRIMARY KEY,
--    name VARCHAR(50)
--);

--INSERT INTO my_schema_old.emp (id, name) VALUES 
--(1, 'Alice'), 
--(2, 'Bob');

--ALTER SCHEMA my_schema_new
--TRANSFER my_schema_old.emp;

--SELECT * FROM my_schema_new.emp;

--USE target_db;

--CREATE SCHEMA my_schema_new;

--SELECT * INTO target_db.my_schema_new.emp FROM source_db.my_schema_new.emp;

--SELECT * FROM my_schema_new.emp;


--Task 3

--USE target_db;

--CREATE LOGIN AuthorizedUser WITH PASSWORD = 'StrongPassword123';
--USE target_db;
--CREATE USER AuthorizedUser FOR LOGIN AuthorizedUser;

--GRANT SELECT, INSERT, UPDATE, DELETE ON SCHEMA::my_schema_new TO AuthorizedUser;

--SELECT princ.name, perm.permission_name, perm.class_desc  
--FROM sys.database_permissions perm  
--JOIN sys.database_principals princ  
--ON perm.grantee_principal_id = princ.principal_id  
--WHERE princ.name = 'AuthorizedUser';

