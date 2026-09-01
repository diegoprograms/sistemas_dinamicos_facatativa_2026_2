from backend.model.validation import require_nonnegative, require_unit_interval


def calculate_production(
    area_ha: float,
    potential_yield_kg_ha: float,
    water_factor: float,
    climate_factor: float,
) -> float:
    require_nonnegative(area_ha, "El área")
    require_nonnegative(potential_yield_kg_ha, "El rendimiento potencial")
    require_unit_interval(water_factor, "El factor hídrico")
    require_unit_interval(climate_factor, "El factor climático")
    return area_ha * potential_yield_kg_ha * water_factor * climate_factor
