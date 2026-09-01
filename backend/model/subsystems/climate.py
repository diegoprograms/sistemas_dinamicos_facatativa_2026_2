from backend.model.validation import require_nonnegative, require_unit_interval


def effective_precipitation(precipitation_mm: float, effective_fraction: float) -> float:
    require_nonnegative(precipitation_mm, "La precipitación")
    require_unit_interval(effective_fraction, "La fracción efectiva")
    return precipitation_mm * effective_fraction
