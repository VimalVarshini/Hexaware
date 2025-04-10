from util.DB_Connect import db_connection

class UserDAOImpl:
    def insert_user(self, user):
        conn = db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO Users (userId, username, password, role) VALUES (?, ?, ?, ?)"
        cursor.execute(query, (user.user_id, user.username, user.password, user.role))
        conn.commit()
        conn.close()

    def get_user_by_id(self, user_id):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Users WHERE userId = ?", (user_id,))
        row = cursor.fetchone()
        conn.close()
        return row

    def get_user_by_username(self, username):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Users WHERE username = ?", (username,))
        row = cursor.fetchone()
        conn.close()
        return row

    def get_all_users(self):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Users")
        rows = cursor.fetchall()
        conn.close()
        return rows
