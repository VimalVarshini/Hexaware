from util.DBConnect import db_connection
from entity.Passenger import Passenger

class PassengerDAOImpl:
    def insert_passenger(self, passenger):
        conn = db_connection()
        cursor = conn.cursor()
        query = """INSERT INTO Passengers 
                   (FirstName, Gender, Age, Email, PhoneNumber) 
                   VALUES (?, ?, ?, ?, ?)"""
        cursor.execute(query, (passenger.first_name, passenger.gender,
                               passenger.age, passenger.email, passenger.phone_number))
        conn.commit()
        conn.close()

    def get_passenger_by_id(self, passenger_id):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Passengers WHERE PassengerID = ?", (passenger_id,))
        row = cursor.fetchone()
        conn.close()
        return row

    def get_all_passengers(self):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Passengers")
        rows = cursor.fetchall()
        conn.close()
        return rows
