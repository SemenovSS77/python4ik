INGREDIENTS = {
    "flour": {"calories": 364, "price_per_kg": 1.5},
    "tomato": {"calories": 18, "price_per_kg": 2.0},
    "cheese": {"calories": 402, "price_per_kg": 10.0},
    "beef": {"calories": 250, "price_per_kg": 8.0},
    "lettuce": {"calories": 15, "price_per_kg": 3.0},
    "noodles": {"calories": 138, "price_per_kg": 2.5},
    "soy_sauce": {"calories": 53, "price_per_kg": 5.0},
    "oil": {"calories": 884, "price_per_kg": 4.0},
}

def get_ingredient_info(ingredient):
    return INGREDIENTS.get(ingredient, {"calories": 0, "price_per_kg": 0})