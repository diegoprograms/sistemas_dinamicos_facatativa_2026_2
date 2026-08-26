def effective_precipitation(precipitation_mm: float, effective_fraction: float) -> float:
    if not 0 <= effective_fraction <= 1:
        raise ValueError("La fracción efectiva debe estar entre 0 y 1")
    return precipitation_mm * effective_fraction

