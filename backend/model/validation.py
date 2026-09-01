def require_nonnegative(value: float, field_name: str) -> float:
    """Valida magnitudes físicas que no pueden ser negativas."""
    if value < 0:
        raise ValueError(f"{field_name} no puede ser negativo")
    return value


def require_unit_interval(value: float, field_name: str) -> float:
    """Valida factores adimensionales expresados entre cero y uno."""
    if not 0 <= value <= 1:
        raise ValueError(f"{field_name} debe estar entre 0 y 1")
    return value
