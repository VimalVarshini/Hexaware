class BookingNotFoundException(Exception):
    def __init__(self, message="Booking not found in the system."):
        super().__init__(message)
