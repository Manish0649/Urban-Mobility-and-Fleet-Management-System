from vehicle import Vehicle

class ElectricCar(Vehicle):
    def __init__(self, vehicle_id, model, battery_percentage, seating_capacity):
        super().__init__(vehicle_id, model, battery_percentage)
        self.seating_capacity = seating_capacity

    def get_seating_capacity(self):
        return self.__seating_capacity

    def set_seating_capacity(self, seating_capacity):
        if seating_capacity > 0:
            self.__seating_capacity = seating_capacity
        else:
            raise ValueError("Seating capacity should be greater than zero")
