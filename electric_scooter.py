from vehicle import Vehicle

class ElectricScooter(Vehicle):
    def __init__(self, vehicle_id, model, battery_percentage,fare_price, max_speed_limit):
        super().__init__(vehicle_id, model, battery_percentage,fare_price)
        self.set_max_speed_limit(max_speed_limit)

    def __repr__(self):
        return f"({self.vehicle_id},{self.model},{self.get_battery_percentage()},{self.get_max_speed_limit()},{self.get_maintenance_status()})"

    def __str__(self):
        return (
            f"Electric Scooter | ID: {self.vehicle_id} | "
            f"Model: {self.model} | Battery: {self.get_battery_percentage()}% | "
            f"Status: {self.get_maintenance_status()} | "
            f"Max Speed: {self.get_max_speed_limit()} | "
            f"Rental Price: ${self.get_rental_price():.2f}"
        )

    def get_max_speed_limit(self):
        return self.__max_speed_limit

    def set_max_speed_limit(self, max_speed_limit):
        if max_speed_limit > 0:
            self.__max_speed_limit = max_speed_limit
        else:
            raise ValueError("Max speed limit should be greater than zero")

    def calculate_trip_cost(self, minutes):
        if minutes < 0:
            raise ValueError("Minutes cannot be negative.")
        return 1 + (0.15 * minutes)