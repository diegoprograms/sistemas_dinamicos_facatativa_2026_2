def validate_nonnegative(value: float, field_name: str) -> float:
    if value < 0:
        raise ValueError(f"{field_name} no puede ser negativo")
    return value

