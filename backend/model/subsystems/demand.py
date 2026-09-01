from backend.model.validation import require_nonnegative


def calculate_required_production(consumption_kg: float, loss_fraction: float) -> float:
    require_nonnegative(consumption_kg, "El consumo")
    if not 0 <= loss_fraction < 1:
        raise ValueError("La fracción de pérdidas debe estar entre 0 y 1")
    return consumption_kg / (1 - loss_fraction)
