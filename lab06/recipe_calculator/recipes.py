RECIPES = {
    "Вок": {
        "ingredients": {
            "noodles": 0.3,  # кг
            "soy_sauce": 0.1,
            "oil": 0.05,
            "beef": 0.2,
        }
    },
    "Бургер": {
        "ingredients": {
            "beef": 0.2,
            "lettuce": 0.05,
            "cheese": 0.05,
            "flour": 0.1,
        }
    },
    "Пицца": {
        "ingredients": {
            "flour": 0.3,
            "tomato": 0.2,
            "cheese": 0.2,
            "oil": 0.05,
        }
    },
}

def get_recipe_ingredients(recipe_name):
    return RECIPES.get(recipe_name, {}).get("ingredients", {})