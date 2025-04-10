from util.DB_Connect import db_connection

class OrderItemDAOImpl:
    def insert_order_item(self, order_item):
        conn = db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO OrderItems (orderId, productId, quantity) VALUES (?, ?, ?)"
        cursor.execute(query, (order_item.order_id, order_item.product_id, order_item.quantity))
        conn.commit()
        conn.close()

    def get_order_items_by_order_id(self, order_id):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM OrderItems WHERE orderId = ?", (order_id,))
        rows = cursor.fetchall()
        conn.close()
        return rows

    def delete_order_items_by_order_id(self, order_id):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM OrderItems WHERE orderId = ?", (order_id,))
        conn.commit()
        conn.close()
