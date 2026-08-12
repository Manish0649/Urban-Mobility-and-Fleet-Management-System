import pytest
from fleet_management import FleetManager
from hub import Hub
from electric_car import ElectricCar
from electric_scooter import ElectricScooter


def test_fleet_manager_creation():
    manager = FleetManager()
    assert manager.hubs == {}


def test_add_hub(monkeypatch):
    manager = FleetManager()
    monkeypatch.setattr("builtins.input", lambda _: "Downtown")
    manager.add_hub()
    assert "downtown" in manager.hubs
    assert manager.hubs["downtown"].name == "Downtown"


def test_add_duplicate_hub(monkeypatch, capsys):
    manager = FleetManager()
    monkeypatch.setattr("builtins.input", lambda _: "Downtown")
    manager.add_hub()
    monkeypatch.setattr("builtins.input", lambda _: "downtown")
    manager.add_hub()
    captured = capsys.readouterr()
    assert "already exists" in captured.out
    assert len(manager.hubs) == 1


def test_add_car_to_hub(monkeypatch):
    manager = FleetManager()
    manager.hubs["downtown"] = Hub("Downtown")
    inputs = iter([
        "Downtown",
        "ElectricCar",
        "C001",
        "BMW",
        "89",
        "50",
        "4",
        "Available"
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    manager.add_vehicle_to_hub()
    vehicles = manager.hubs["downtown"].vehicles
    assert len(vehicles) == 1
    assert isinstance(vehicles[0], ElectricCar)
    assert vehicles[0].vehicle_id == "C001"
    assert vehicles[0].model == "BMW"


def test_add_scooter_to_hub(monkeypatch):
    manager = FleetManager()
    manager.hubs["downtown"] = Hub("Downtown")
    inputs = iter([
        "Downtown",
        "ElectricScooter",
        "S001",
        "Ola",
        "85",
        "30",
        "60",
        "Available"
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    manager.add_vehicle_to_hub()
    vehicles = manager.hubs["downtown"].vehicles
    assert len(vehicles) == 1
    assert isinstance(vehicles[0], ElectricScooter)
    assert vehicles[0].vehicle_id == "S001"


def create_test_manager():
    manager = FleetManager()
    hub = Hub("Downtown")
    car1 = ElectricCar("C001", "BMW", 90, 50, 4)
    car2 = ElectricCar("C002", "Tesla", 70, 80, 5)
    scooter = ElectricScooter("S001", "Ola", 85, 30, 60)
    car2.set_maintenance_status("On Trip")
    scooter.set_maintenance_status("Under Maintenance")
    hub.add_vehicle(car1)
    hub.add_vehicle(car2)
    hub.add_vehicle(scooter)
    manager.hubs["downtown"] = hub
    return manager


def test_search_vehicle_in_hub(monkeypatch, capsys):
    manager = create_test_manager()
    monkeypatch.setattr("builtins.input", lambda _: "Downtown")
    manager.search_vehicle_in_hub()
    captured = capsys.readouterr()
    assert "C001" in captured.out
    assert "C002" in captured.out
    assert "S001" in captured.out


def test_search_vehicle_by_battery(monkeypatch, capsys):
    manager = create_test_manager()
    monkeypatch.setattr("builtins.input", lambda _: "Downtown")
    manager.search_vehicle_by_battery()
    captured = capsys.readouterr()
    assert "C001" in captured.out
    assert "S001" in captured.out
    # C002 has 70%, so it should not appear
    assert "C002" not in captured.out


def test_view_vehicles_by_type(monkeypatch, capsys):
    manager = create_test_manager()
    monkeypatch.setattr("builtins.input", lambda _: "Downtown")
    manager.view_vehicles_by_type()
    captured = capsys.readouterr()
    assert "C001" in captured.out
    assert "C002" in captured.out
    assert "S001" in captured.out
    assert "Cars:" in captured.out
    assert "Scooters:" in captured.out


def test_vehicle_count_by_status(monkeypatch, capsys):
    manager = create_test_manager()
    monkeypatch.setattr("builtins.input", lambda _: "Downtown")
    manager.get_vehicle_count_by_status()
    captured = capsys.readouterr()
    assert "Available: 1" in captured.out
    assert "On Trip: 1" in captured.out
    assert "Under Maintenance: 1" in captured.out


def test_sort_by_model_name(monkeypatch, capsys):
    manager = create_test_manager()
    monkeypatch.setattr("builtins.input", lambda _: "Downtown")
    manager.get_vehicles_sorted_by_modelname()
    captured = capsys.readouterr()
    bmw_position = captured.out.index("BMW")
    ola_position = captured.out.index("Ola")
    tesla_position = captured.out.index("Tesla")
    assert bmw_position < ola_position < tesla_position


def test_sort_by_battery(monkeypatch, capsys):
    manager = create_test_manager()
    monkeypatch.setattr("builtins.input", lambda _: "Downtown")
    manager.sort_vehicles_by("battery")
    captured = capsys.readouterr()
    # Battery order should be 90 -> 85 -> 70
    first = captured.out.index("BMW")
    second = captured.out.index("Ola")
    third = captured.out.index("Tesla")
    assert first < second < third


def test_sort_by_fare(monkeypatch, capsys):
    manager = create_test_manager()
    monkeypatch.setattr("builtins.input", lambda _: "Downtown")
    manager.sort_vehicles_by("fare")
    captured = capsys.readouterr()
    # Fare order should be 80 -> 50 -> 30
    first = captured.out.index("Tesla")
    second = captured.out.index("BMW")
    third = captured.out.index("Ola")
    assert first < second < third


def test_invalid_sort_attribute(monkeypatch, capsys):
    manager = create_test_manager()
    monkeypatch.setattr("builtins.input", lambda _: "Downtown")
    manager.sort_vehicles_by("speed")
    captured = capsys.readouterr()
    assert "Invalid attribute" in captured.out


def test_save_to_csv(tmp_path):
    manager = create_test_manager()
    csv_file = tmp_path / "test_fleet.csv"
    manager.save_to_csv(csv_file)
    assert csv_file.exists()
    content = csv_file.read_text()
    assert "Downtown" in content
    assert "C001" in content
    assert "C002" in content
    assert "S001" in content


def test_load_from_csv(tmp_path):
    manager = create_test_manager()
    csv_file = tmp_path / "test_fleet.csv"
    manager.save_to_csv(csv_file)
    new_manager = FleetManager()
    new_manager.load_from_csv(csv_file)
    assert "downtown" in new_manager.hubs
    vehicles = new_manager.hubs["downtown"].vehicles
    assert len(vehicles) == 3
    assert isinstance(vehicles[0], ElectricCar)
    assert isinstance(vehicles[1], ElectricCar)
    assert isinstance(vehicles[2], ElectricScooter)


def test_csv_preserves_vehicle_data(tmp_path):
    manager = create_test_manager()
    csv_file = tmp_path / "test_fleet.csv"
    manager.save_to_csv(csv_file)
    new_manager = FleetManager()
    new_manager.load_from_csv(csv_file)
    vehicles = new_manager.hubs["downtown"].vehicles
    car = vehicles[0]
    scooter = vehicles[2]
    assert car.vehicle_id == "C001"
    assert car.model == "BMW"
    assert car.get_battery_percentage() == 90
    assert car.get_rental_price() == 50
    assert car.get_seating_capacity() == 4
    assert scooter.vehicle_id == "S001"
    assert scooter.model == "Ola"
    assert scooter.get_battery_percentage() == 85
    assert scooter.get_rental_price() == 30
    assert scooter.get_max_speed_limit() == 60


def test_csv_preserves_maintenance_status(tmp_path):
    manager = create_test_manager()
    csv_file = tmp_path / "test_fleet.csv"
    manager.save_to_csv(csv_file)
    new_manager = FleetManager()
    new_manager.load_from_csv(csv_file)
    vehicles = new_manager.hubs["downtown"].vehicles
    assert vehicles[0].get_maintenance_status() == "Available"
    assert vehicles[1].get_maintenance_status() == "On Trip"
    assert vehicles[2].get_maintenance_status() == "Under Maintenance"


def test_save_to_json(tmp_path):
    manager = create_test_manager()
    json_file = tmp_path / "test_fleet.json"
    manager.save_to_json(json_file)
    assert json_file.exists()
    content = json_file.read_text()
    assert "Downtown" in content
    assert "C001" in content
    assert "C002" in content
    assert "S001" in content


def test_load_from_json(tmp_path):
    manager = create_test_manager()
    json_file = tmp_path / "test_fleet.json"
    manager.save_to_json(json_file)
    new_manager = FleetManager()
    new_manager.load_from_json(json_file)
    assert "downtown" in new_manager.hubs
    vehicles = new_manager.hubs["downtown"].vehicles
    assert len(vehicles) == 3
    assert isinstance(vehicles[0], ElectricCar)
    assert isinstance(vehicles[1], ElectricCar)
    assert isinstance(vehicles[2], ElectricScooter)


def test_json_preserves_car_data(tmp_path):
    manager = create_test_manager()
    json_file = tmp_path / "test_fleet.json"
    manager.save_to_json(json_file)
    new_manager = FleetManager()
    new_manager.load_from_json(json_file)
    car = new_manager.hubs["downtown"].vehicles[0]
    assert car.vehicle_id == "C001"
    assert car.model == "BMW"
    assert car.get_battery_percentage() == 90
    assert car.get_maintenance_status() == "Available"
    assert car.get_rental_price() == 50
    assert car.get_seating_capacity() == 4


def test_json_preserves_scooter_data(tmp_path):
    manager = create_test_manager()
    json_file = tmp_path / "test_fleet.json"
    manager.save_to_json(json_file)
    new_manager = FleetManager()
    new_manager.load_from_json(json_file)
    scooter = new_manager.hubs["downtown"].vehicles[2]
    assert scooter.vehicle_id == "S001"
    assert scooter.model == "Ola"
    assert scooter.get_battery_percentage() == 85
    assert scooter.get_maintenance_status() == "Under Maintenance"
    assert scooter.get_rental_price() == 30
    assert scooter.get_max_speed_limit() == 60


def test_json_preserves_nested_hub_vehicle_relationship(tmp_path):
    manager = create_test_manager()
    json_file = tmp_path / "test_fleet.json"
    manager.save_to_json(json_file)
    new_manager = FleetManager()
    new_manager.load_from_json(json_file)
    hub = new_manager.hubs["downtown"]
    assert hub.name == "Downtown"
    assert len(hub.vehicles) == 3
    vehicle_ids = [vehicle.vehicle_id for vehicle in hub.vehicles]
    assert "C001" in vehicle_ids
    assert "C002" in vehicle_ids
    assert "S001" in vehicle_ids