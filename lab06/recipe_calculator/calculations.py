from .ingredients import get_ingredient_info

def calculate_calories(ingredients):
    total_calories = 0
    for ingredient, amount in ingredients.items():
        info = get_ingredient_info(ingredient)
        total_calories += info["calories"] * amount
    return total_calories

def calculate_cost(ingredients):
    total_cost = 0
    for ingredient, amount in ingredients.items():
        info = get_ingredient_info(ingredient)
        total_cost += info["price_per_kg"] * amount
    return total_cost