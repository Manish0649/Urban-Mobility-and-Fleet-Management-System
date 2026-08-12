import pytest
from electric_scooter import ElectricScooter


def test_electric_scooter_creation():
    scooter = ElectricScooter("S001", "Ola", 85, 30, 60)
    assert scooter.vehicle_id == "S001"
    assert scooter.model == "Ola"
    assert scooter.get_battery_percentage() == 85
    assert scooter.get_rental_price() == 30
    assert scooter.get_max_speed_limit() == 60


def test_max_speed_limit():
    scooter = ElectricScooter("S001", "Ola", 85, 30, 60)
    scooter.set_max_speed_limit(70)
    assert scooter.get_max_speed_limit() == 70


def test_invalid_max_speed_limit():
    with pytest.raises(ValueError):
        ElectricScooter("S001", "Ola", 85, 30, 0)


def test_negative_max_speed_limit():
    with pytest.raises(ValueError):
        ElectricScooter("S001", "Ola", 85, 30, -10)


def test_scooter_trip_cost():
    scooter = ElectricScooter("S001", "Ola", 85, 30, 60)
    assert scooter.calculate_trip_cost(10) == 2.5


def test_scooter_trip_cost_zero_minutes():
    scooter = ElectricScooter("S001", "Ola", 85, 30, 60)
    assert scooter.calculate_trip_cost(0) == 1


def test_scooter_trip_cost_negative_minutes():
    scooter = ElectricScooter("S001", "Ola", 85, 30, 60)
    with pytest.raises(ValueError):
        scooter.calculate_trip_cost(-10)


def test_scooter_string():
    scooter = ElectricScooter("S001", "Ola", 85, 30, 60)
    result = str(scooter)
    assert "Electric Scooter" in result
    assert "S001" in result
    assert "Ola" in result
    assert "85%" in result
    assert "Available" in result
    assert "Max Speed: 60" in result
    assert "$30.00" in result


def test_scooter_repr():
    scooter = ElectricScooter("S001", "Ola", 85, 30, 60)
    result = repr(scooter)
    assert result == "(S001,Ola,85,60,Available)"