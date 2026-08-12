import pytest
from electric_car import ElectricCar


def test_electric_car_creation():
    car = ElectricCar("C001", "BMW", 89, 50, 4)
    assert car.vehicle_id == "C001"
    assert car.model == "BMW"
    assert car.get_battery_percentage() == 89
    assert car.get_rental_price() == 50
    assert car.get_seating_capacity() == 4


def test_seating_capacity():
    car = ElectricCar("C001", "BMW", 89, 50, 4)
    car.set_seating_capacity(5)
    assert car.get_seating_capacity() == 5


def test_invalid_seating_capacity():
    with pytest.raises(ValueError):
        ElectricCar("C001", "BMW", 89, 50, 0)


def test_negative_seating_capacity():
    with pytest.raises(ValueError):
        ElectricCar("C001", "BMW", 89, 50, -2)


def test_car_trip_cost():
    car = ElectricCar("C001", "BMW", 89, 50, 4)
    assert car.calculate_trip_cost(10) == 10.0


def test_car_trip_cost_zero_distance():
    car = ElectricCar("C001", "BMW", 89, 50, 4)
    assert car.calculate_trip_cost(0) == 5.0


def test_car_trip_cost_negative_distance():
    car = ElectricCar("C001", "BMW", 89, 50, 4)
    with pytest.raises(ValueError):
        car.calculate_trip_cost(-10)


def test_car_string():
    car = ElectricCar("C001", "BMW", 89, 50, 4)
    result = str(car)
    assert "C001" in result
    assert "BMW" in result
    assert "89%" in result
    assert "Available" in result
    assert "Seating Capacity: 4" in result
    assert "$50.00" in result


def test_car_repr():
    car = ElectricCar("C001", "BMW", 89, 50, 4)
    result = repr(car)
    assert result == "(C001,BMW,89,4,Available)"