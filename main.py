from electric_car import ElectricCar
from electric_scooter import ElectricScooter

def main():
    print("Welcome to Eco-Ride Urban Mobility System")

    scooter = ElectricScooter("S001", "Ola", 90, 70)
    car = ElectricCar("C001", "BMW", 85, 4)

    print("Electric Scooter")
    print("Vehicle ID:", scooter.vehicle_id)
    print("Model:", scooter.model)
    print("Battery:", scooter.get_battery_percentage())
    print("Max Speed:", scooter.get_max_speed_limit())

    print()

    print("Electric Car")
    print("Vehicle ID:", car.vehicle_id)
    print("Model:", car.model)
    print("Battery:", car.get_battery_percentage())
    print("Seating Capacity:", car.get_seating_capacity())


if __name__ == "__main__":
    main()