from entity.Customer import Customer
from entity.Accounts import Account
from entity.Transaction import Transaction
from dao.CustomerDAOImpl import CustomerDAOImpl
from dao.AccountDAOImpl import AccountDAOImpl
from dao.TransactionDAOImpl import TransactionDAOImpl
from datetime import datetime

customer_dao = CustomerDAOImpl()
account_dao = AccountDAOImpl()
transaction_dao = TransactionDAOImpl()

def menu():
    print("\n===== Banking Menu =====")
    print("1. Register Customer")
    print("2. Open Bank Account")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. View All Customers")
    print("6. View All Accounts")
    print("7. View Transactions by Account")
    print("8. Transfer Between Accounts")
    print("9. Exit")

# Main loop
while True:
    menu()
    choice = input("Enter your choice: ")

    # Register a new customer
    if choice == '1':
        customer = Customer(
            None,
            input("First Name: "),
            input("Last Name: "),
            input("DOB (YYYY-MM-DD): "),
            input("Email: "),
            input("Phone: "),
            input("Address: ")
        )
        customer_dao.insert_customer(customer)
        print("✅ Customer registered.")

    # Open new account
    elif choice == '2':
        cust_id = int(input("Customer ID: "))
        row = customer_dao.get_customer_by_id(cust_id)
        if not row:
            print("❌ Customer not found.")
        else:
            acc_type = input("Account Type (savings/current/zero_balance): ").lower()
            balance = float(input("Initial Balance: "))

            # Apply account creation rules
            if acc_type == 'savings' and balance < 500:
                print("❌ Savings account requires a minimum balance of ₹500.")
                continue
            elif acc_type == 'zero_balance' and balance != 0:
                print("❌ Zero balance account must be opened with ₹0 balance.")
                continue

            customer = Customer(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            account = Account(None, customer, acc_type, balance)
            account_dao.insert_account(account)
            print("✅ Account created.")

    # Deposit money
    elif choice == '3':
        acc_id = int(input("Account ID: "))
        row = account_dao.get_account_by_id(acc_id)
        if not row:
            print("❌ Account not found.")
        else:
            amount = float(input("Amount to deposit: "))
            if amount <= 0:
                print("❌ Deposit amount must be greater than ₹0.")
                continue

            current_balance = float(row[3])
            new_balance = current_balance + amount
            account_dao.update_balance(acc_id, new_balance)
            transaction_dao.insert_transaction(Transaction(acc_id, "deposit", amount, "Deposit"))
            print(f"✅ Deposited ₹{amount:.2f}. New Balance: ₹{new_balance:.2f}")

    # Withdraw money
    elif choice == '4':
        acc_id = int(input("Account ID: "))
        row = account_dao.get_account_by_id(acc_id)
        if not row:
            print("❌ Account not found.")
        else:
            amount = float(input("Amount to withdraw: "))
            current_balance = float(row[3])
            if amount > current_balance:
                print("❌ Insufficient funds.")
            else:
                new_balance = current_balance - amount
                account_dao.update_balance(acc_id, new_balance)
                transaction_dao.insert_transaction(Transaction(acc_id, "withdrawal", amount, "Withdrawal"))
                print(f"✅ Withdrawn ₹{amount:.2f}. New Balance: ₹{new_balance:.2f}")

    # Show all customers
    elif choice == '5':
        customers = customer_dao.get_all_customers()
        for c in customers:
            print(f"ID: {c[0]} | Name: {c[1]} {c[2]} | D.O.B: {c[3]} | Email: {c[4]} | Phone: {c[5]} | Address: {c[6]}")

    # Show all accounts
    elif choice == '6':
        accounts = account_dao.get_all_accounts()
        for a in accounts:
            print(f"Account ID: {a[0]} | Customer ID: {a[1]} | Type: {a[2]} | Balance: ₹{float(a[3]):.2f}")

    # View transactions for an account
    elif choice == '7':
        acc_id = int(input("Account ID: "))
        txns = transaction_dao.get_transactions_by_account(acc_id)
        if not txns:
            print("❌ No transactions found.")
        else:
            for t in txns:
                print(f"[{t[4]}] {t[2].capitalize()} ₹{t[3]:.2f} — {t[5]}")

    # Transfer money between accounts
    elif choice == '8':
        from_acc = int(input("From Account ID: "))
        to_acc = int(input("To Account ID: "))
        amount = float(input("Amount to transfer: "))

        from_row = account_dao.get_account_by_id(from_acc)
        to_row = account_dao.get_account_by_id(to_acc)

        if not from_row or not to_row:
            print("❌ One or both accounts not found.")
        else:
            from_balance = float(from_row[3])
            to_balance = float(to_row[3])

            if from_balance < amount:
                print("❌ Insufficient funds in source account.")
            else:
                new_from_balance = from_balance - amount
                new_to_balance = to_balance + amount

                account_dao.update_balance(from_acc, new_from_balance)
                account_dao.update_balance(to_acc, new_to_balance)

                transaction_dao.insert_transaction(Transaction(from_acc, "transfer", amount, f"Transferred to {to_acc}"))
                transaction_dao.insert_transaction(Transaction(to_acc, "transfer", amount, f"Received from {from_acc}"))

                print("✅ Transfer successful.")

    # Exit the program
    elif choice == '9':
        print("👋 Thank you for using our Bank. Goodbye!")
        break

    else:
        print("❌ Invalid option. Please try again.")
