import csv
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
                fare_price = float(input("Enter Fare Price: "))
                seating_capacity = int(input("Enter Seating Capacity: "))
                maintenance_status = input("Enter maintenance status (Available / On Trip / Under Maintenance) [Available]: ").strip() or "Available"
                vehicle = ElectricCar(vehicle_id, model, battery_percentage, fare_price, seating_capacity)
                vehicle.set_maintenance_status(maintenance_status)

            elif vehicle_type == "electricscooter":
                vehicle_id = input("Enter Vehicle ID: ")
                model = input("Enter Model: ")
                battery_percentage = int(input("Enter Battery Percentage: "))
                fare_price = float(input("Enter Fare Price: "))
                max_speed = int(input("Enter Max Speed: "))
                maintenance_status = input("Enter maintenance status (Available / On Trip / Under Maintenance) [Available]: ").strip() or "Available"
                vehicle = ElectricScooter(vehicle_id, model, battery_percentage, fare_price, max_speed)
                vehicle.set_maintenance_status(maintenance_status)

            
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


    def get_vehicle_count_by_status(self):
        hub_name = input("Enter Hub name to get vehicle count by status: ")
        hub_key = hub_name.strip().lower()
        hub = self.hubs.get(hub_key)
        if not hub:
            print(f"Hub {hub_name} does not exist.")
            return

        status_count = {"Available": 0, "On Trip": 0, "Under Maintenance": 0}

        for vehicle in hub.vehicles:
            status = vehicle.get_maintenance_status()
            if status in status_count:
                status_count[status] += 1

        print(f"Vehicle count by status in Hub {hub_name}:")
        for status, count in status_count.items():
            print(f"  {status}: {count}")

    def get_vehicles_sorted_by_modelname(self):
        hub_name = input("Enter Hub name to get vehicles sorted by model name: ")
        hub_key = hub_name.strip().lower()
        hub = self.hubs.get(hub_key)
        if not hub:
            print(f"Hub {hub_name} does not exist.")
            return

        sorted_vehicles = sorted(hub.vehicles, key=lambda v: v.model.lower())

        print(f"\nVehicles in Hub {hub_name} sorted by model name:")
        for vehicle in sorted_vehicles:
            print(vehicle)
        print("\n")


    def sort_vehicles_by(self,attribute):
        hub_name = input("Enter Hub name to sort vehicles: ")
        hub_key = hub_name.strip().lower()
        hub = self.hubs.get(hub_key)
        if not hub:
            print(f"Hub {hub_name} does not exist.")
            return

        attribute = attribute.strip().lower()
        if attribute == "battery":
            sorted_vehicles = sorted(hub.vehicles, key = lambda v:v.get_battery_percentage(), reverse = True)
            title = "sorted by battery percentage (descending):"

        elif attribute == "fare":
            sorted_vehicles = sorted(hub.vehicles, key = lambda v:v.get_rental_price(), reverse = True)
            title = "sorted by fare price (descending):"

        else:
            print("Invalid attribute. Please choose 'battery' or 'fare'.")
            return

        print(f"\nVehicles in Hub {hub_name} {title}")
        for vehicle in sorted_vehicles:
            print(vehicle)
        
    def save_to_csv(self, filename="fleet.csv"):
        fieldnames = [
            "hub_name",
            "vehicle_type",
            "vehicle_id",
            "model",
            "battery_percentage",
            "maintenance_status",
            "rental_price",
            "seating_capacity",
            "max_speed_limit",
        ]
        with open(filename, mode="w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for hub in self.hubs.values():
                for vehicle in hub.vehicles:
                    row = {
                        "hub_name": hub.name,
                        "vehicle_type": type(vehicle).__name__,
                        "vehicle_id": vehicle.vehicle_id,
                        "model": vehicle.model,
                        "battery_percentage": vehicle.get_battery_percentage(),
                        "maintenance_status": vehicle.get_maintenance_status(),
                        "rental_price": vehicle.get_rental_price(),
                        "seating_capacity": "",
                        "max_speed_limit": "",
                    }
                    if isinstance(vehicle, ElectricCar):
                        row["seating_capacity"] = vehicle.get_seating_capacity()
                    elif isinstance(vehicle, ElectricScooter):
                        row["max_speed_limit"] = vehicle.get_max_speed_limit()
                    writer.writerow(row)

    def load_from_csv(self, filename="fleet.csv"):
        try:
            with open(filename, mode="r", newline="", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    hub_name = row["hub_name"].strip()
                    hub_key = hub_name.lower()
                    hub = self.hubs.setdefault(hub_key, Hub(hub_name))

                    if row["vehicle_type"] == "ElectricCar":
                        vehicle = ElectricCar(
                            row["vehicle_id"],
                            row["model"],
                            int(row["battery_percentage"]),
                            float(row["rental_price"] or 0),
                            int(row["seating_capacity"]),
                        )
                    elif row["vehicle_type"] == "ElectricScooter":
                        vehicle = ElectricScooter(
                            row["vehicle_id"],
                            row["model"],
                            int(row["battery_percentage"]),
                            float(row["rental_price"] or 0),
                            int(row["max_speed_limit"]),
                        )
                    else:
                        continue

                    vehicle.set_maintenance_status(row["maintenance_status"] or "Available")
                    vehicle.set_rental_price(float(row["rental_price"] or 0))
                    hub.add_vehicle(vehicle)
        except FileNotFoundError:
            pass