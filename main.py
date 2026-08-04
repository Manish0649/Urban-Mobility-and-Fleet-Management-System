from vehicle import Vehicle
from electric_scooter import ElectricScooter
from electric_car import ElectricCar

def main():

    print("Welcome to the Urban Mobility and Fleet Management System")

    # Create a Vehicle object
    vehicle1 = Vehicle(vehicle_id="V001", model="Tesla", battery_percentage=85)

    # Print vehicle details
    print(f"Battery Percentage: {vehicle1.get_battery_percentage()}")
    vehicle1.set_maintenance_status("all good")
    print(f"Maintenance Status: {vehicle1.get_maintenance_status()}")
    vehicle1.set_rental_price(50)
    print(f"Rental Price: {vehicle1.get_rental_price()}")

    scooter1 = ElectricScooter(123,"Ola",90,70)
    print(f"Max Speed Limit: {scooter1.get_max_speed_limit()}")
    
    electric_car1 = ElectricCar(1,"BMW",90,4)
    print(f"Seating Capacity: {electric_car1.get_seating_capacity()}")

if __name__ == "__main__":
    main()