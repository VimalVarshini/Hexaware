class PassengerNotFoundException(Exception):
    def __init__(self, message="Passenger not found in the system."):
        super().__init__(message)
