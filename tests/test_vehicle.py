import pytest
from electric_car import ElectricCar


def test_battery_percentage():
    car = ElectricCar("C001", "BMW", 89, 50, 4)
    assert car.get_battery_percentage() == 89


def test_battery_percentage_validation():
    with pytest.raises(ValueError):
        ElectricCar("C001", "BMW", 101, 50, 4)


def test_battery_percentage_negative():
    with pytest.raises(ValueError):
        ElectricCar("C001", "BMW", -1, 50, 4)


def test_maintenance_status():
    car = ElectricCar("C001", "BMW", 89, 50, 4)
    assert car.get_maintenance_status() == "Available"
    car.set_maintenance_status("On Trip")
    assert car.get_maintenance_status() == "On Trip"


def test_invalid_maintenance_status():
    car = ElectricCar("C001", "BMW", 89, 50, 4)
    with pytest.raises(ValueError):
        car.set_maintenance_status("Broken")


def test_rental_price():
    car = ElectricCar("C001", "BMW", 89, 50, 4)
    assert car.get_rental_price() == 50


def test_negative_rental_price():
    with pytest.raises(ValueError):
        ElectricCar("C001", "BMW", 89, -10, 4)


def test_vehicle_equality():
    car1 = ElectricCar("C001", "BMW", 89, 50, 4)
    car2 = ElectricCar("C001", "Tesla", 50, 30, 2)
    assert car1 == car2


def test_vehicle_inequality():
    car1 = ElectricCar("C001", "BMW", 89, 50, 4)
    car2 = ElectricCar("C002", "BMW", 89, 50, 4)
    assert car1 != car2