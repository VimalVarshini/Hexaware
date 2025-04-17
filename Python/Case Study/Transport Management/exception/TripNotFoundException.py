class TripNotFoundException(Exception):
    def __init__(self, message="Trip not found in the system."):
        super().__init__(message)
