from backend.model.indicators import food_gap, water_gap


def run_preliminary_model(
    consumption_kg: float,
    available_supply_kg: float,
    required_water_m3: float,
    available_water_m3: float,
) -> dict:
    """Integra resultados preliminares de los subsistemas.

    Esta función no representa todavía el modelo dinámico completo. Será
    reemplazada gradualmente por niveles, flujos, retrasos y realimentaciones.
    """
    return {
        "food_gap_kg": food_gap(consumption_kg, available_supply_kg),
        "water_gap_m3": water_gap(required_water_m3, available_water_m3),
    }

