class InvalidAccountException(Exception):
    """
    Raised when an invalid or non-existent account number is used.
    """
    def __init__(self, message="The account number provided is invalid or does not exist."):
        super().__init__(message)


class InsufficientFundException(Exception):
    """
    Raised when there are not enough funds for a withdrawal or transfer.
    """
    def __init__(self, message="Insufficient funds in the account to complete the transaction."):
        super().__init__(message)


class OverDraftLimitExceededException(Exception):
    """
    Raised when withdrawal exceeds allowed overdraft limit in a current account.
    """
    def __init__(self, message="Withdrawal amount exceeds the overdraft limit for this account."):
        super().__init__(message)


class MinimumBalanceViolationException(Exception):
    """
    Raised when withdrawal leads to balance going below required minimum (e.g. for savings).
    """
    def __init__(self, message="Withdrawal violates the minimum balance requirement."):
        super().__init__(message)