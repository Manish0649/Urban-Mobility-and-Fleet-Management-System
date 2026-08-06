from electric_car import ElectricCar
from electric_scooter import ElectricScooter
from fleet_management import FleetManager


def main():

    print("Welcome to Eco-Ride Urban Mobility System")

    car1 = ElectricCar("C001", "BMW", 90, 4)
    car2 = ElectricCar("C002", "Tesla", 95, 5)
    scooter1 = ElectricScooter("S001", "Ola", 85, 70)
    scooter2 = ElectricScooter("S002", "Ather", 80, 60)

    # vehicles = [car, scooter]

    # for vehicle in vehicles:
    #     print(vehicle.calculate_trip_cost(20))

    fleet_manager = FleetManager()
    fleet_manager.add_hub()
    fleet_manager.add_vehicle_to_hub()
    fleet_manager.add_vehicle_to_hub()
    fleet_manager.search_vehicle_in_hub()
    fleet_manager.search_vehicle_by_battery()


if __name__ == "__main__":
    main()