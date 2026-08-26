def calculate_production(
    area_ha: float,
    potential_yield_kg_ha: float,
    water_factor: float,
    climate_factor: float,
) -> float:
    return area_ha * potential_yield_kg_ha * water_factor * climate_factor

