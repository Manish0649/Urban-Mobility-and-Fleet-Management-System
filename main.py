from electric_car import ElectricCar
from electric_scooter import ElectricScooter


def main():

    print("Welcome to Eco-Ride Urban Mobility System")

    car = ElectricCar("C001", "BMW", 90, 4)
    scooter = ElectricScooter("S001", "Ola", 85, 70)

    vehicles = [car, scooter]

    for vehicle in vehicles:
        print(vehicle.calculate_trip_cost(20))


if __name__ == "__main__":
    main()