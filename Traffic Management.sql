--CREATE DATABASE transport_management;

--USE transport_management;

--CREATE TABLE Vehicles (
--    vehicle_id INT IDENTITY(1,1) PRIMARY KEY,
--    model NVARCHAR(50) NOT NULL,
--    capacity INT NOT NULL
--);

--INSERT INTO Vehicles (model, capacity) VALUES ('Volvo Bus', 50);
--INSERT INTO Vehicles (model, capacity) VALUES ('Mercedes Sprinter', 20);

--CREATE TABLE Routes (
--    route_id INT IDENTITY(1,1) PRIMARY KEY,
--    source NVARCHAR(100) NOT NULL,
--    destination NVARCHAR(100) NOT NULL,
--    distance INT NOT NULL
--);

--INSERT INTO Routes (source, destination, distance) VALUES ('New York', 'Washington DC', 350);
--INSERT INTO Routes (source, destination, distance) VALUES ('Los Angeles', 'San Francisco', 600);


--CREATE TABLE Trips (
--    trip_id INT IDENTITY(1,1) PRIMARY KEY,
--    vehicle_id INT NOT NULL,
--    route_id INT NOT NULL,
--    departure_date DATE NOT NULL,
--    arrival_date DATE NOT NULL,
--    FOREIGN KEY (vehicle_id) REFERENCES Vehicles(vehicle_id),
--    FOREIGN KEY (route_id) REFERENCES Routes(route_id)
--);

--INSERT INTO Trips (vehicle_id, route_id, departure_date, arrival_date) 
--VALUES (1, 1, '2025-04-01', '2025-04-02');

--CREATE TABLE Passengers (
--    passenger_id INT IDENTITY(1,1) PRIMARY KEY,
--    name NVARCHAR(100) NOT NULL,
--    email NVARCHAR(100) UNIQUE NOT NULL
--);

--INSERT INTO Passengers (name, email) VALUES ('John Doe', 'john@example.com');
--INSERT INTO Passengers (name, email) VALUES ('Alice Brown', 'alice@example.com');

--CREATE TABLE Bookings (
--    booking_id INT IDENTITY(1,1) PRIMARY KEY,
--    trip_id INT NOT NULL,
--    passenger_id INT NOT NULL,
--    booking_date DATE NOT NULL,
--    FOREIGN KEY (trip_id) REFERENCES Trips(trip_id),
--    FOREIGN KEY (passenger_id) REFERENCES Passengers(passenger_id)
--);

--INSERT INTO Bookings (trip_id, passenger_id, booking_date) 
--VALUES (1, 1, '2025-03-30');


--CREATE TABLE Drivers (
--    driver_id INT IDENTITY(1,1) PRIMARY KEY,
--    name NVARCHAR(100) NOT NULL,
--    license_number NVARCHAR(50) UNIQUE NOT NULL
--);

--INSERT INTO Drivers (name, license_number) VALUES ('Jane Smith', 'D12345');
--INSERT INTO Drivers (name, license_number) VALUES ('Bob Williams', 'D67890');

--CREATE TABLE Driver_Allocation (
--    allocation_id INT IDENTITY(1,1) PRIMARY KEY,
--    trip_id INT NOT NULL,
--    driver_id INT NOT NULL,
--    FOREIGN KEY (trip_id) REFERENCES Trips(trip_id),
--    FOREIGN KEY (driver_id) REFERENCES Drivers(driver_id)
--);

--INSERT INTO Driver_Allocation (trip_id, driver_id) VALUES (1, 1);

--SELECT * FROM Vehicles;

--SELECT T.trip_id, V.model AS Vehicle, R.source, R.destination, T.departure_date, T.arrival_date
--FROM Trips T
--JOIN Vehicles V ON T.vehicle_id = V.vehicle_id
--JOIN Routes R ON T.route_id = R.route_id;

--SELECT B.booking_id, P.name AS Passenger, T.trip_id, R.source, R.destination, B.booking_date
--FROM Bookings B
--JOIN Passengers P ON B.passenger_id = P.passenger_id
--JOIN Trips T ON B.trip_id = T.trip_id
--JOIN Routes R ON T.route_id = R.route_id
--WHERE P.passenger_id = 1;

--SELECT * FROM Drivers 
--WHERE driver_id NOT IN (SELECT driver_id FROM Driver_Allocation);


--DELETE FROM Bookings WHERE booking_id = 1;

--UPDATE Trips
--SET departure_date = '2025-04-05', arrival_date = '2025-04-06'
--WHERE trip_id = 1;

