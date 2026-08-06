from collections import defaultdict
from electric_car import ElectricCar
from electric_scooter import ElectricScooter
from hub import Hub

class FleetManager:

    def __init__(self):
        self.hubs = {}

    def add_hub(self):
        hub_name = input("Enter Hub name: ")
        hub_key = hub_name.strip().lower()
        if hub_key in self.hubs:
            print(f"Hub {hub_name} already exists.")
        else:
            self.hubs[hub_key] = Hub(hub_name)
            print(f"Hub {hub_name} added.")

    def add_vehicle_to_hub(self):
        hub_name = input("Enter Hub name to add vehicle: ")
        hub_key = hub_name.strip().lower()
        hub = self.hubs.get(hub_key)
        if not hub:
            print(f"Hub {hub_name} does not exist.")
            return
        else:
            vehicle_type = input("Enter vehicle type (ElectricCar / ElectricScooter): ").strip().lower()
            if vehicle_type == "electriccar":
                vehicle_id = input("Enter Vehicle ID: ")
                model = input("Enter Model: ")
                battery_percentage = int(input("Enter Battery Percentage: "))
                seating_capacity = int(input("Enter Seating Capacity: "))
                vehicle = ElectricCar(vehicle_id, model, battery_percentage, seating_capacity)

            elif vehicle_type == "electricscooter":
                vehicle_id = input("Enter Vehicle ID: ")
                model = input("Enter Model: ")
                battery_percentage = int(input("Enter Battery Percentage: "))
                max_speed = int(input("Enter Max Speed: "))
                vehicle = ElectricScooter(vehicle_id, model, battery_percentage, max_speed)

            else:
                print("Invalid vehicle type.")
                return

            success, msg = hub.add_vehicle(vehicle)
        print(msg)
        if success:
            # print format: {'Downtown': [(id,model,battery,seat),]}
            print({hub.name: hub.vehicles})

    def search_vehicle_in_hub(self):
        hub_name = input("Enter Hub name to search vehicle: ")
        hub_key = hub_name.strip().lower()
        hub = self.hubs.get(hub_key)
        if not hub:
            print(f"Hub {hub_name} does not exist.")
            return 
        vehicles = hub.vehicles
        if not vehicles:
            print(f"No vehicles found in Hub {hub_name}.")
            return

        print(f"Vehicles in Hub {hub_name}:")
        for vehicle in vehicles:
            print(vehicle)


    def search_vehicle_by_battery(self):
        hub_name = input("Enter Hub name to search vehicle by battery percentage: ")
        hub_key = hub_name.strip().lower()
        hub = self.hubs.get(hub_key)
        if not hub:
            print(f"Hub {hub_name} does not exist.")
            return

        vehicles = hub.vehicles
        if not vehicles:
            print(f"No vehicles found in Hub {hub_name}.")
            return

        high_battery_vehicles = list(filter(lambda v: v.get_battery_percentage() > 80, vehicles))
        if not high_battery_vehicles:
            print(f"No vehicles with battery percentage greater than 80% found in Hub {hub_name}.")
            return

        print(f"Vehicles with battery percentage greater than 80% in Hub {hub_name}:")
        for vehicle in high_battery_vehicles:
            print(vehicle)  


    def view_vehicles_by_type(self):
        hub_name = input("Enter Hub name to view vehicles by type: ")
        hub_key = hub_name.strip().lower()
        hub = self.hubs.get(hub_key)
        if not hub:
            print(f"Hub {hub_name} does not exist.")
            return

        grouped_vehicles = defaultdict(list)

        for vehicle in hub.vehicles:
            if isinstance(vehicle, ElectricCar):
                grouped_vehicles['ElectricCar'].append(vehicle)
            elif isinstance(vehicle, ElectricScooter):
                grouped_vehicles['ElectricScooter'].append(vehicle)

        print("\nCars:")
        if grouped_vehicles['ElectricCar']:
            for car in grouped_vehicles['ElectricCar']:
                print(car)
        else:
            print("No Electric Cars found.")

        print("\nScooters:")
        if grouped_vehicles['ElectricScooter']:
            for scooter in grouped_vehicles['ElectricScooter']:
                print(scooter)
        else:
            print("No Electric Scooters found.")


