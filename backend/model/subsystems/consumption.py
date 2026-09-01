from backend.model.validation import require_nonnegative


def calculate_consumption(dishes_sold: float, kg_per_dish: float) -> float:
    require_nonnegative(dishes_sold, "Los platos vendidos")
    require_nonnegative(kg_per_dish, "Los kilogramos por plato")
    return dishes_sold * kg_per_dish
