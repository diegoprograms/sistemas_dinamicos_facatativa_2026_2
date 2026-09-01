from backend.model.validation import require_nonnegative


def food_gap(required_consumption_kg: float, available_supply_kg: float) -> float:
    require_nonnegative(required_consumption_kg, "El consumo requerido")
    require_nonnegative(available_supply_kg, "La oferta disponible")
    return required_consumption_kg - available_supply_kg


def water_gap(required_water_m3: float, available_water_m3: float) -> float:
    require_nonnegative(required_water_m3, "El agua requerida")
    require_nonnegative(available_water_m3, "El agua disponible")
    return required_water_m3 - available_water_m3


def water_productivity(production_kg: float, used_water_m3: float) -> float:
    require_nonnegative(production_kg, "La producción")
    if used_water_m3 <= 0:
        raise ValueError("El agua utilizada debe ser mayor que cero")
    return production_kg / used_water_m3
