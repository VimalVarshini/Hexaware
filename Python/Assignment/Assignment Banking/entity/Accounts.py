class Account:
    def __init__(self, account_id=None, customer=None, account_type="", balance=0.0):
        self.account_id = account_id
        self.customer = customer
        self.account_type = account_type
        self.balance = balance
        self.transactions = []