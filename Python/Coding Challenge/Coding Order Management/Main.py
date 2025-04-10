from entity.Users import Users
from entity.Products import Products
from entity.Electronics import Electronics
from entity.Clothing import Clothing
from entity.OrderItem import OrderItem
from dao.UserDAOImpl import UserDAOImpl
from dao.ProductDAOImpl import ProductDAOImpl
from dao.ClothingDAOImpl import ClothingDAOImpl
from dao.ElectronicsDAOImpl import ElectronicsDAOImpl
from dao.OrderDAOImpl import OrderDAOImpl
from dao.OrderItemDAOImpl import OrderItemDAOImpl

def display_menu():
    print("\n==== ORDER MANAGEMENT SYSTEM ====")
    print("1. Create User")
    print("2. Create Product")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Create Order")
    print("6. Cancel Order")
    print("7. View User by ID")
    print("8. View All Users")
    print("9. View Product by ID")
    print("10. View All Products")
    print("11. View Orders by User")
    print("12. View All Orders")
    print("13. View Order Items by Order ID")
    print("14. Exit")

def main():
    user_dao = UserDAOImpl()
    product_dao = ProductDAOImpl()
    clothing_dao = ClothingDAOImpl()
    electronics_dao = ElectronicsDAOImpl()
    order_dao = OrderDAOImpl()
    order_item_dao = OrderItemDAOImpl()

    while True:
        display_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            user_id = int(input("User ID: "))
            username = input("Username: ")
            password = input("Password: ")
            role = input("Role (Admin/User): ")
            user = Users(user_id, username, password, role)
            user_dao.insert_user(user)
            print("User created.")

        elif choice == "2":
            admin_id = int(input("Enter Admin User ID: "))
            admin_user = user_dao.get_user_by_id(admin_id)
            if not admin_user or admin_user[3].lower() != 'admin':
                print("Only Admins can create products.")
                continue

            product_id = int(input("Product ID: "))
            name = input("Product Name: ")
            desc = input("Description: ")
            price = float(input("Price: "))
            stock = int(input("Quantity In Stock: "))
            ptype = input("Type (Electronics/Clothing): ")

            if ptype.lower() == "electronics":
                brand = input("Brand: ")
                warranty = int(input("Warranty (months): "))
                product = Electronics(product_id, name, desc, price, stock, brand, warranty)
                product_dao.insert_product(product)
                electronics_dao.insert_electronics(product)

            elif ptype.lower() == "clothing":
                size = input("Size: ")
                color = input("Color: ")
                product = Clothing(product_id, name, desc, price, stock, size, color)
                product_dao.insert_product(product)
                clothing_dao.insert_clothing(product)

            else:
                print("Invalid product type.")
                continue
            print("Product added.")

        elif choice == "3":
            pid = int(input("Product ID: "))
            pname = input("New Product Name: ")
            desc = input("New Description: ")
            price = float(input("New Price: "))
            stock = int(input("New Stock: "))
            ptype = input("Type (Electronics/Clothing): ")
            product = Products(pid, pname, desc, price, stock, ptype)
            product_dao.update_product(product)
            print("Product updated.")

        elif choice == "4":
            pid = int(input("Product ID to delete: "))
            clothing_dao.delete_clothing(pid)
            electronics_dao.delete_electronics(pid)
            product_dao.delete_product(pid)
            print("Product deleted.")

        elif choice == "5":
            uid = int(input("User ID: "))
            username = input("Username: ")
            password = input("Password: ")
            user = Users(uid, username, password, "User")

            ids = input("Enter product IDs (comma separated): ").split(",")
            product_list = []
            for pid in ids:
                prod = product_dao.get_product_by_id(int(pid))
                if prod:
                    product_list.append(Products(*prod))
            order_dao.create_order(user, product_list)
            print("Order placed.")

        elif choice == "6":
            uid = int(input("User ID: "))
            oid = int(input("Order ID: "))
            order_dao.cancel_order(uid, oid)
            print("Order cancelled.")

        elif choice == "7":
            uid = int(input("Enter user ID: "))
            user = user_dao.get_user_by_id(uid)
            print(user)

        elif choice == "8":
            users = user_dao.get_all_users()
            for u in users:
                print(u)

        elif choice == "9":
            pid = int(input("Product ID: "))
            product = product_dao.get_product_by_id(pid)
            print(product)

        elif choice == "10":
            products = product_dao.get_all_products()
            for p in products:
                print(p)

        elif choice == "11":
            uid = int(input("User ID: "))
            username = input("Username: ")
            password = input("Password: ")
            user = Users(uid, username, password, "User")
            orders = order_dao.get_order_by_user(user)
            if not orders:
                print("No orders found for this user.")
            else:
                print("\nOrder Details:")
                current_order_id = None
                for order in orders:
                    order_id, order_date, product_id, product_name, quantity = order
                    if order_id != current_order_id:
                        print(f"\n🧾 Order ID: {order_id} | Date: {order_date}")
                        current_order_id = order_id
                    print(f"   ➤ Product: {product_name} (ID: {product_id}) | Quantity: {quantity}")

        elif choice == "12":
            orders = order_dao.get_all_orders()
            if not orders:
                print("No orders found.")
            else:
                print("\nAll Order Details:")
                current_order_id = None
                for order in orders:
                    order_id, order_date, user_id, username, product_id, product_name, quantity = order
                    if order_id != current_order_id:
                        print(f"\n🧾 Order ID: {order_id} | Date: {order_date} | User: {username} (ID: {user_id})")
                        current_order_id = order_id
                    print(f"   ➤ Product: {product_name} (ID: {product_id}) | Quantity: {quantity}")

        elif choice == "13":
            oid = int(input("Order ID: "))
            items = order_item_dao.get_order_items_by_order_id(oid)
            for item in items:
                print(item)

        elif choice == "14":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
