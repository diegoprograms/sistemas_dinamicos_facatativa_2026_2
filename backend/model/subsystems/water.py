def available_water(
    stored_water_m3: float,
    effective_rain_m3: float,
    irrigation_input_m3: float,
    losses_m3: float,
    other_uses_m3: float,
) -> float:
    result = (
        stored_water_m3
        + effective_rain_m3
        + irrigation_input_m3
        - losses_m3
        - other_uses_m3
    )
    return max(0.0, result)

