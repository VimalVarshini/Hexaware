from util.DB_Connect import db_connection

class ClothingDAOImpl:
    def insert_clothing(self, clothing):
        conn = db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO Clothing (productId, size, color) VALUES (?, ?, ?)"
        cursor.execute(query, (clothing.product_id, clothing.size, clothing.color))
        conn.commit()
        conn.close()

    def get_clothing_by_id(self, product_id):
        conn = db_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM Clothing WHERE productId = ?"
        cursor.execute(query, (product_id,))
        row = cursor.fetchone()
        conn.close()
        return row

    def update_clothing(self, clothing):
        conn = db_connection()
        cursor = conn.cursor()
        query = "UPDATE Clothing SET size = ?, color = ? WHERE productId = ?"
        cursor.execute(query, (clothing.size, clothing.color, clothing.product_id))
        conn.commit()
        conn.close()

    def delete_clothing(self, product_id):
        conn = db_connection()
        cursor = conn.cursor()
        query = "DELETE FROM Clothing WHERE productId = ?"
        cursor.execute(query, (product_id,))
        conn.commit()
        conn.close()

    def get_all_clothing(self):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Clothing")
        rows = cursor.fetchall()
        conn.close()
        return rows
