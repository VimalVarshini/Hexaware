from util.DBConnect import db_connection
from entity.Vehicle import Vehicle

class VehicleDAOImpl:
    def insert_vehicle(self, vehicle):
        conn = db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO Vehicles (Model, Capacity, Type, Status) VALUES (?, ?, ?, ?)"
        cursor.execute(query, (vehicle.model, vehicle.capacity, vehicle.v_type, vehicle.status))
        conn.commit()
        conn.close()

    def get_vehicle_by_id(self, vehicle_id):
        conn = db_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM Vehicles WHERE VehicleID = ?"
        cursor.execute(query, (vehicle_id,))
        row = cursor.fetchone()
        conn.close()
        return row

    def update_vehicle(self, vehicle):
        conn = db_connection()
        cursor = conn.cursor()
        query = "UPDATE Vehicles SET Model = ?, Capacity = ?, Type = ?, Status = ? WHERE VehicleID = ?"
        cursor.execute(query, (vehicle.model, vehicle.capacity, vehicle.v_type, vehicle.status, vehicle.vehicle_id))
        conn.commit()
        conn.close()

    def delete_vehicle(self, vehicle_id):
        conn = db_connection()
        cursor = conn.cursor()
        query = "DELETE FROM Vehicles WHERE VehicleID = ?"
        cursor.execute(query, (vehicle_id,))
        conn.commit()
        conn.close()

    def get_all_vehicles(self):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Vehicles")
        rows = cursor.fetchall()
        conn.close()
        return rows
