def calculate_supply(
    local_production_kg: float,
    external_supply_kg: float,
    loss_fraction: float,
) -> float:
    if not 0 <= loss_fraction < 1:
        raise ValueError("La fracción de pérdidas debe estar entre 0 y 1")
    return (local_production_kg + external_supply_kg) * (1 - loss_fraction)

