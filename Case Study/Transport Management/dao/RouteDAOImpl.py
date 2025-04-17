from util.DBConnect import db_connection
from entity.Route import Route

class RouteDAOImpl:
    def insert_route(self, route):
        conn = db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO Routes (StartDestination, EndDestination, Distance) VALUES (?, ?, ?)"
        cursor.execute(query, (route.start_destination, route.end_destination, route.distance))
        conn.commit()
        conn.close()

    def get_route_by_id(self, route_id):
        conn = db_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM Routes WHERE RouteID = ?"
        cursor.execute(query, (route_id,))
        row = cursor.fetchone()
        conn.close()
        return row

    def get_all_routes(self):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Routes")
        rows = cursor.fetchall()
        conn.close()
        return rows
