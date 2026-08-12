import pytest
from hub import Hub
from electric_car import ElectricCar
from electric_scooter import ElectricScooter


def test_hub_creation():
    hub = Hub("Downtown")
    assert hub.name == "Downtown"
    assert hub.vehicles == []


def test_add_car_to_hub():
    hub = Hub("Downtown")
    car = ElectricCar("C001", "BMW", 89, 50, 4)
    success, message = hub.add_vehicle(car)
    assert success is True
    assert car in hub.vehicles
    assert message == "Vehicle C001 added to Hub Downtown successfully."


def test_add_scooter_to_hub():
    hub = Hub("Downtown")
    scooter = ElectricScooter("S001", "Ola", 85, 30, 60)
    success, message = hub.add_vehicle(scooter)
    assert success is True
    assert scooter in hub.vehicles


def test_duplicate_vehicle_id():
    hub = Hub("Downtown")
    car1 = ElectricCar("C001", "BMW", 89, 50, 4)
    car2 = ElectricCar("C001", "Tesla", 90, 60, 5)
    success1, message1 = hub.add_vehicle(car1)
    success2, message2 = hub.add_vehicle(car2)
    assert success1 is True
    assert success2 is False
    assert len(hub.vehicles) == 1
    assert "C001" in message2
    assert "already exists" in message2


def test_multiple_vehicles():
    hub = Hub("Downtown")
    car = ElectricCar("C001", "BMW", 89, 50, 4)
    scooter = ElectricScooter("S001", "Ola", 85, 30, 60)
    hub.add_vehicle(car)
    hub.add_vehicle(scooter)
    assert len(hub.vehicles) == 2
    assert car in hub.vehicles
    assert scooter in hub.vehicles
