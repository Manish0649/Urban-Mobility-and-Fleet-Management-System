class Hub:
    def __init__(self, name):
        self.name = name
        self.vehicles = []

    def add_vehicle(self, vehicle):
        if any(v.vehicle_id == vehicle.vehicle_id for v in self.vehicles):
            return False, f"a vehicle with id {vehicle.vehicle_id} already exists in the {self.name} hub"
        self.vehicles.append(vehicle)

        return True, f"Vehicle {vehicle.vehicle_id} added to Hub {self.name} successfully."
    