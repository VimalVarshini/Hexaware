class Trip:
    def __init__(self, trip_id=None, vehicle=None, route=None,
                 departure_date=None, arrival_date=None,
                 status="Scheduled", trip_type="Freight", max_passengers=0):
        self.trip_id = trip_id
        self.vehicle = vehicle
        self.route = route
        self.departure_date = departure_date
        self.arrival_date = arrival_date
        self.status = status
        self.trip_type = trip_type
        self.max_passengers = max_passengers
