from vehicle import Vehicle

def main():

    print("Welcome to the Urban Mobility and Fleet Management System")
    # Create a Vehicle object
    vehicle1 = Vehicle(vehicle_id="V001", model="Tesla", battery_percentage=85)

    # Print vehicle details
    print(f"Vehicle ID: {vehicle1.vehicle_id}")
    print(f"Model: {vehicle1.model}")
    print(f"Battery Percentage: {vehicle1.battery_percentage}%")

if __name__ == "__main__":
    main()