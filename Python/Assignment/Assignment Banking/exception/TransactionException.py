class TransactionFailedException(Exception):
    """
    Raised when a transaction (deposit/withdrawal/transfer) fails to process or save.
    """
    def __init__(self, message="Transaction could not be completed."):
        super().__init__(message)


class TransactionNotFoundException(Exception):
    """
    Raised when attempting to fetch a transaction that doesn't exist.
    """
    def __init__(self, message="No transactions found for the given criteria."):
        super().__init__(message)