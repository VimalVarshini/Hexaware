from util.DBConnect import db_connection
from entity.Booking import Booking

class BookingDAOImpl:
    def insert_booking(self, booking):
        conn = db_connection()
        cursor = conn.cursor()
        query = """INSERT INTO Bookings 
                   (TripID, PassengerID, BookingDate, Status) 
                   VALUES (?, ?, ?, ?)"""
        cursor.execute(query, (booking.trip.trip_id, booking.passenger.passenger_id,
                               booking.booking_date, booking.status))
        conn.commit()
        conn.close()

    def cancel_booking(self, booking_id):
        conn = db_connection()
        cursor = conn.cursor()
        query = "UPDATE Bookings SET Status = 'Cancelled' WHERE BookingID = ?"
        cursor.execute(query, (booking_id,))
        conn.commit()
        conn.close()

    def get_booking_by_id(self, booking_id):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Bookings WHERE BookingID = ?", (booking_id,))
        row = cursor.fetchone()
        conn.close()
        return row

    def get_bookings_by_passenger(self, passenger_id):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Bookings WHERE PassengerID = ?", (passenger_id,))
        rows = cursor.fetchall()
        conn.close()
        return rows

    def get_bookings_by_trip(self, trip_id):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Bookings WHERE TripID = ?", (trip_id,))
        rows = cursor.fetchall()
        conn.close()
        return rows
