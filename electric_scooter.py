from vehicle import Vehicle

class ElectricScooter(Vehicle):
    def __init__(self, vehicle_id, model, battery_percentage, max_speed_limit):
        super().__init__(vehicle_id, model, battery_percentage)
        self.set_max_speed_limit(max_speed_limit)

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