def consumption_to_required_water(
    consumption_kg: float,
    yield_kg_ha: float,
    water_need_m3_ha: float,
) -> tuple[float, float]:
    """Conecta consumo, área requerida y agua requerida."""
    if yield_kg_ha <= 0:
        raise ValueError("El rendimiento debe ser mayor que cero")

    required_area_ha = consumption_kg / yield_kg_ha
    required_water_m3 = required_area_ha * water_need_m3_ha
    return required_area_ha, required_water_m3

