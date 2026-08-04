from vehicle import Vehicle

def main():

    print("Welcome to the Urban Mobility and Fleet Management System")

    # Create a Vehicle object
    vehicle1 = Vehicle(vehicle_id="V001", model="Tesla", battery_percentage=85)

    # Print vehicle details
    print(vehicle1.get_battery_percentage())
    vehicle1.set_maintenance_status("all good")
    print(vehicle1.get_maintenance_status())
    vehicle1.set_rental_price(50)
    print(vehicle1.get_rental_price())

if __name__ == "__main__":
    main()