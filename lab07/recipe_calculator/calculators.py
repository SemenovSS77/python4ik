from abc import ABC, abstractmethod

class Calculator(ABC):
    # Абстрактный базовый класс для калькуляторов
    def __init__(self, ingredient_manager):
        self.ingredient_manager = ingredient_manager

    @abstractmethod
    def calculate(self, ingredients):
        pass # 

    def __str__(self):
        return f"Calculator: {self.__class__.__name__}" # Строковое представление

    def __repr__(self):
        return f"<{self.__class__.__name__}>" # Офф строковое представление


class CaloriesCalculator(Calculator): # Наследование от Calculator
    # Класс для расчета калорий
    def calculate(self, ingredients):
        total_calories = 0
        for ingredient, amount in ingredients.items():
            info = self.ingredient_manager.ingredients.get(ingredient, {"calories": 0})
            total_calories += info["calories"] * amount
        return total_calories


class CostCalculator(Calculator): # Наследование от Calculator
    # Класс для расчета стоимости
    def calculate(self, ingredients): 
        total_cost = 0
        for ingredient, amount in ingredients.items():
            info = self.ingredient_manager.ingredients.get(ingredient, {"price_per_kg": 0})
            total_cost += info["price_per_kg"] * amount
        return total_cost