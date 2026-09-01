from backend.model.validation import require_nonnegative


def available_water(
    stored_water_m3: float,
    effective_rain_m3: float,
    irrigation_input_m3: float,
    losses_m3: float,
    other_uses_m3: float,
) -> float:
    for value, field_name in (
        (stored_water_m3, "El agua almacenada"),
        (effective_rain_m3, "La lluvia efectiva"),
        (irrigation_input_m3, "La entrada de riego"),
        (losses_m3, "Las pérdidas de agua"),
        (other_uses_m3, "Los otros usos de agua"),
    ):
        require_nonnegative(value, field_name)

    result = (
        stored_water_m3
        + effective_rain_m3
        + irrigation_input_m3
        - losses_m3
        - other_uses_m3
    )
    return max(0.0, result)
