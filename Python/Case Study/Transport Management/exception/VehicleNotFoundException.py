class VehicleNotFoundException(Exception):
    def __init__(self, message="Vehicle not found in the system."):
        super().__init__(message)
