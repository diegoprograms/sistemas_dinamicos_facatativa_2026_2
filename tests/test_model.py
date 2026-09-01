import pytest

from backend.model.couplings import consumption_to_required_water
from backend.model.indicators import food_gap, water_gap, water_productivity
from backend.model.subsystems.climate import effective_precipitation
from backend.model.subsystems.consumption import calculate_consumption
from backend.model.subsystems.demand import calculate_required_production
from backend.model.subsystems.production import calculate_production
from backend.model.subsystems.supply import calculate_supply
from backend.model.subsystems.water import available_water


def test_consumption_to_required_water():
    area, water = consumption_to_required_water(2000, 20000, 6000)
    assert area == 0.1
    assert water == 600


def test_gaps():
    assert food_gap(1000, 850) == 150
    assert water_gap(300, 240) == 60


def test_water_productivity():
    assert water_productivity(2000, 500) == 4


def test_subsystem_calculations():
    assert calculate_consumption(60, 0.120) == pytest.approx(7.2)
    assert calculate_required_production(90, 0.1) == 100
    assert effective_precipitation(100, 0.8) == 80
    assert calculate_production(2, 1000, 0.8, 0.5) == 800
    assert calculate_supply(800, 200, 0.1) == 900
    assert available_water(100, 50, 20, 10, 30) == 130


def test_available_water_cannot_be_negative():
    assert available_water(10, 0, 0, 20, 0) == 0


@pytest.mark.parametrize(
    ("function", "arguments"),
    [
        (calculate_consumption, (-1, 0.120)),
        (calculate_required_production, (100, 1)),
        (effective_precipitation, (-1, 0.8)),
        (calculate_production, (1, 1000, 1.1, 0.5)),
        (calculate_supply, (-1, 200, 0.1)),
        (available_water, (100, 50, 20, -1, 30)),
        (consumption_to_required_water, (-1, 1000, 500)),
        (water_productivity, (-1, 100)),
    ],
)
def test_invalid_physical_values_raise_value_error(function, arguments):
    with pytest.raises(ValueError):
        function(*arguments)
