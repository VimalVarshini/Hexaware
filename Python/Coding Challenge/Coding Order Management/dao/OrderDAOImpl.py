from util.DB_Connect import db_connection
from exception.User_not_found_exception import UserNotFoundException
from exception.Order_not_found_exception import OrderNotFoundException

class OrderDAOImpl:
    def create_order(self, user, product_list):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Orders (userId) VALUES (?)", (user.user_id,))
        cursor.execute("SELECT SCOPE_IDENTITY()")
        order_id = cursor.fetchone()[0]
        for product in product_list:
            cursor.execute("INSERT INTO OrderItems (orderId, productId, quantity) VALUES (?, ?, ?)",
                           (order_id, product.product_id, 1))

        conn.commit()
        conn.close()

    def cancel_order(self, user_id, order_id):
        conn = db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Users WHERE userId = ?", (user_id,))
        if not cursor.fetchone():
            raise UserNotFoundException("User not found.")

        cursor.execute("SELECT * FROM Orders WHERE orderId = ?", (order_id,))
        if not cursor.fetchone():
            raise OrderNotFoundException("Order not found.")

        cursor.execute("DELETE FROM OrderItems WHERE orderId = ?", (order_id,))
        cursor.execute("DELETE FROM Orders WHERE orderId = ?", (order_id,))
        conn.commit()
        conn.close()

    def get_order_by_id(self, order_id):
        conn = db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Orders WHERE orderId = ?", (order_id,))
        order = cursor.fetchone()
        conn.close()
        return order

    def get_order_by_user(self, user):
        conn = db_connection()
        cursor = conn.cursor()
        query = """
        SELECT o.orderId, o.orderDate, p.productId, p.productName, oi.quantity
        FROM Orders o
        JOIN OrderItems oi ON o.orderId = oi.orderId
        JOIN Products p ON oi.productId = p.productId
        WHERE o.userId = ?
        ORDER BY o.orderId
        """
        cursor.execute(query, (user.user_id,))
        rows = cursor.fetchall()
        conn.close()
        return rows

    def get_all_orders(self):
        conn = db_connection()
        cursor = conn.cursor()
        query = """
        SELECT o.orderId, o.orderDate, u.userId, u.username,
               p.productId, p.productName, oi.quantity
        FROM Orders o
        JOIN Users u ON o.userId = u.userId
        JOIN OrderItems oi ON o.orderId = oi.orderId
        JOIN Products p ON oi.productId = p.productId
        ORDER BY o.orderId
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()
        return rows

