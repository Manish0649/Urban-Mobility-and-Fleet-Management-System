from electric_car import ElectricCar
from electric_scooter import ElectricScooter

class FleetManager:

    def __init__(self):
        self.hubs = {}

    def add_hub(self):
        hub_name = input("Enter Hub name: ")
        if hub_name in self.hubs:
            print(f"Hub {hub_name} already exists.")
        else:
            self.hubs[hub_name] = []
            print(f"Hub {hub_name} added.")

    def add_vehicle_to_hub(self):
        hub_name = input("Enter Hub name to add vehicle: ")
        if hub_name not in self.hubs:
            print(f"Hub {hub_name} does not exist.")
            return
        else:
            vehicle_type = input("Enter vehicle type (ElectricCar / ElectricScooter): ")
            if vehicle_type.lower() == "electriccar":
                vehicle_id = input("Enter Vehicle ID: ")
                model = input("Enter Model: ")
                battery_percentage = int(input("Enter Battery Percentage: "))
                seating_capacity = int(input("Enter Seating Capacity: "))
                vehicle = ElectricCar(vehicle_id, model, battery_percentage, seating_capacity)

            elif vehicle_type.lower() == "electricscooter":
                vehicle_id = input("Enter Vehicle ID: ")
                model = input("Enter Model: ")
                battery_percentage = int(input("Enter Battery Percentage: "))
                max_speed = int(input("Enter Max Speed: "))
                vehicle = ElectricScooter(vehicle_id, model, battery_percentage, max_speed)

            self.hubs[hub_name].append(vehicle)
            print(f"Vehicle {vehicle_id} added to Hub {hub_name} successfully.")
            print({hub_name: self.hubs[hub_name]})  # Print the hubs dictionary to show the added vehicle



