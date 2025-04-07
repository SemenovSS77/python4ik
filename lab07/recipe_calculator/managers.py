# Managed - атрибуты

class IngredientManager:
    # Класс для управления ингредиентами
    def __init__(self):
        self._ingredients = {
            "flour": {"calories": 364, "price_per_kg": 1.5},
            "tomato": {"calories": 18, "price_per_kg": 2.0},
            "cheese": {"calories": 402, "price_per_kg": 10.0},
            "beef": {"calories": 250, "price_per_kg": 8.0},
            "lettuce": {"calories": 15, "price_per_kg": 3.0},
            "noodles": {"calories": 138, "price_per_kg": 2.5},
            "soy_sauce": {"calories": 53, "price_per_kg": 5.0},
            "oil": {"calories": 884, "price_per_kg": 4.0},
        }

    @property # геттер
    def ingredients(self):
        return self._ingredients

    @ingredients.setter # сеттер
    def ingredients(self, value):
        raise AttributeError("Ингредиенты нельзя изменять напрямую")

    def __len__(self):
        return len(self._ingredients)

    def __contains__(self, item):
        return item in self._ingredients

    def __str__(self):
        return f"IngredientManager with {len(self)} ingredients"


class RecipeManager:
    # Класс для управления рецептами
    def __init__(self):
        self._recipes = {
            "Вок": {
                "ingredients": {
                    "noodles": 0.3,
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

    @property # геттер
    def recipes(self):
        return self._recipes

    @recipes.setter # сеттер
    def recipes(self, value):
        raise AttributeError("Рецепты нельзя изменять напрямую")

    def __len__(self):
        return len(self._recipes)

    def __contains__(self, item):
        return item in self._recipes

    def __str__(self):
        return f"RecipeManager with {len(self)} recipes"