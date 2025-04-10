class DuplicateEntryException(Exception):
    def __init__(self, message="Duplicate entry found"):
        super().__init__(message)
