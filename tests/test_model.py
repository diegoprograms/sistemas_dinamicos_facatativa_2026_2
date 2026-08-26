from backend.model.couplings import consumption_to_required_water
from backend.model.indicators import food_gap, water_gap, water_productivity


def test_consumption_to_required_water():
    area, water = consumption_to_required_water(2000, 20000, 6000)
    assert area == 0.1
    assert water == 600


def test_gaps():
    assert food_gap(1000, 850) == 150
    assert water_gap(300, 240) == 60


def test_water_productivity():
    assert water_productivity(2000, 500) == 4

