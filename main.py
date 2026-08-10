from fleet_management import FleetManager


def print_menu():
    print("\nEco-Ride Urban Mobility System")
    print("1. Add a Hub")
    print("2. Add a Vehicle to Hub")
    print("3. Search Vehicles in a Hub")
    print("4. Search Vehicles by Battery > 80%")
    print("5. View Vehicles by Type")
    print("6. Get Vehicle Count by Maintenance Status")
    print("7. Get Vehicles Sorted by Model Name")
    print("8. Sort Vehicles by Battery Percentage")
    print("9. Sort Vehicles by Fare Price")
    print("10. Save Fleet to CSV")
    print("11. Load Fleet from CSV")
    print("0. Exit")


def main():
    fleet_manager = FleetManager()
    fleet_manager.load_from_csv("fleet.csv")

    while True:
        print_menu()
        choice = input("Enter option number: ").strip()

        if choice == "1":
            fleet_manager.add_hub()
        elif choice == "2":
            fleet_manager.add_vehicle_to_hub()
        elif choice == "3":
            fleet_manager.search_vehicle_in_hub()
        elif choice == "4":
            fleet_manager.search_vehicle_by_battery()
        elif choice == "5":
            fleet_manager.view_vehicles_by_type()
        elif choice == "6":
            fleet_manager.get_vehicle_count_by_status()
        elif choice == "7":
            fleet_manager.get_vehicles_sorted_by_modelname()
        elif choice == "8":
            fleet_manager.sort_vehicles_by("battery")
        elif choice == "9":
            fleet_manager.sort_vehicles_by("fare")
        elif choice == "10":
            fleet_manager.save_to_csv("fleet.csv")
            print("Fleet data saved to fleet.csv.")
        elif choice == "11":
            fleet_manager.load_from_csv("fleet.csv")
            print("Fleet data loaded from fleet.csv.")
        elif choice == "0":
            fleet_manager.save_to_csv("fleet.csv")
            print("Fleet data saved. Exiting.")
            break
        else:
            print("Invalid option. Please enter a number from 0 to 11.")


if __name__ == "__main__":
    main()