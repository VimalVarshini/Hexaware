class Vehicle:
    def __init__(self, vehicle_id=None, model="", capacity=0.0, v_type="", status="Available"):
        self.vehicle_id = vehicle_id
        self.model = model
        self.capacity = capacity
        self.v_type = v_type
        self.status = status
