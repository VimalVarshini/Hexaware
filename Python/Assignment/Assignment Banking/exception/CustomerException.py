class CustomerNotFoundException(Exception):
    """
    Raised when a customer is not found in the system.
    """
    def __init__(self, message="Customer not found with the given ID."):
        super().__init__(message)


class DuplicateCustomerException(Exception):
    """
    Raised when trying to add a customer that already exists.
    """
    def __init__(self, message="Customer already exists in the system."):
        super().__init__(message)