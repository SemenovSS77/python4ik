from .ingredients import INGREDIENTS, get_ingredient_info
from .recipes import RECIPES, get_recipe_ingredients
from .calculations import calculate_calories, calculate_cost
from .database import init_db, save_calculation, get_stats

# Инициализация БД при первом импорте
init_db()