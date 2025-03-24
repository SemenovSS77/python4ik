# Проделанная работа
## main.py
Создали файл main.py, в котором сделали функции save_to_docx и save_to_xlsx 
для сохранения результатов в формате .docx и .xlsx.  
Сделали функцию on_calculate для вычисления калорий и стоимости.  
Создали переменную app, которая создает окно 400x300, список с рецептами, добавляет кнопки (обрабатываются функцией on_calculate),
а также ниже добавляет поля для вывода результатов.

## dir: recipe_calculator
### __init__.py
Импортирует функции из модулей, чтобы их можно было использовать в main.py
### ingredients.py
Создали словарь INGREDIENTS, в котором написаны названия ингредиентов, калорийности и цена за кг.  
Сделали функцию get_ingredient_info, которая возвращает информацию об ингредиенте или же "{"calories": 0, "price_per_kg": 0}", если его нет.
### recipes.py
Создали словарь RECIPES, где для каждого указаны ингредиенты и их кол-во.  
Сделали функцию get_recipe_ingredients, которая возвращает ингредиенты для выбранного рецепта.
### calculations.py
Сделали функцию calculate_calories, которая считает калории всех ингредиентов, учитвая их количество.  
Создали функцию calculate_cost, которая аналогично рассчитывает стоимость рецепта.

# Результат
![image](https://github.com/user-attachments/assets/5203eaf6-f0ab-49ad-95df-141d2316e6a7)


# Ссылки на материалы
## [docx](https://pydocs.ru/python-docx/)  
## [openpyxl](https://docs-python.ru/packages/modul-openpyxl/)  
## [appjar](https://python-scripts.com/pdf-splitter-appjar?ysclid=m8neqs5do7978227377)  
