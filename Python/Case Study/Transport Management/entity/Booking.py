class Booking:
    def __init__(self, booking_id=None, trip=None, passenger=None,
                 booking_date=None, status="Confirmed"):
        self.booking_id = booking_id
        self.trip = trip
        self.passenger = passenger
        self.booking_date = booking_date
        self.status = status
