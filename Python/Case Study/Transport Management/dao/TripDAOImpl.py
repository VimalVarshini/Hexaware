from util.DBConnect import db_connection
from entity.Trip import Trip

class TripDAOImpl:
    def schedule_trip(self, trip):
        conn = db_connection()
        cursor = conn.cursor()
        query = """INSERT INTO Trips 
                   (VehicleID, RouteID, DepartureDate, ArrivalDate, Status, TripType, MaxPassengers)
                   VALUES (?, ?, ?, ?, ?, ?, ?)"""
        cursor.execute(query, (trip.vehicle.vehicle_id, trip.route.route_id,
                               trip.departure_date, trip.arrival_date,
                               trip.status, trip.trip_type, trip.max_passengers))
        conn.commit()
        conn.close()

    def cancel_trip(self, trip_id):
        conn = db_connection()
        cursor = conn.cursor()
        query = "UPDATE Trips SET Status = 'Cancelled' WHERE TripID = ?"
        cursor.execute(query, (trip_id,))
        conn.commit()
        conn.close()

    def get_trip_by_id(self, trip_id):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Trips WHERE TripID = ?", (trip_id,))
        row = cursor.fetchone()
        conn.close()
        return row

    def get_all_trips(self):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Trips")
        rows = cursor.fetchall()
        conn.close()
        return rows
