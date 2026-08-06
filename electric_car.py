from turtle import distance

from vehicle import Vehicle

class ElectricCar(Vehicle):
    def __init__(self, vehicle_id, model, battery_percentage, seating_capacity):
        super().__init__(vehicle_id, model, battery_percentage)
        self.__seating_capacity = None
        self.set_seating_capacity(seating_capacity)

    def __repr__(self):
        return f"({self.vehicle_id},{self.model},{self.get_battery_percentage()},{self.get_seating_capacity()},{self.get_maintenance_status()})"

    def get_seating_capacity(self):
        return self.__seating_capacity

    def set_seating_capacity(self, seating_capacity):
        if seating_capacity > 0:
            self.__seating_capacity = seating_capacity
        else:
            raise ValueError("Seating capacity should be greater than zero")

    def calculate_trip_cost(self, distance):
        if distance < 0:
            raise ValueError("Distance cannot be negative.")
        return 5 + (0.5 * distance)
            
