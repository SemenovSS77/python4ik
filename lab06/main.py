from appJar import gui
from recipe_calculator import get_recipe_ingredients, calculate_calories, calculate_cost
from docx import Document
from openpyxl import Workbook

def save_to_docx(recipe_name, calories, cost):
    doc = Document()
    doc.add_heading(f"Рецепт: {recipe_name}", 0)
    doc.add_paragraph(f"Энергетическая ценность: {calories} ккал")
    doc.add_paragraph(f"Стоимость: {cost} $")
    doc.save(f"{recipe_name}_report.docx")

def save_to_xlsx(recipe_name, calories, cost):
    wb = Workbook()
    ws = wb.active
    ws.title = "Отчет"
    ws['A1'] = "Рецепт"
    ws['B1'] = recipe_name
    ws['A2'] = "Энергетическая ценность"
    ws['B2'] = calories
    ws['A3'] = "Стоимость"
    ws['B3'] = cost
    wb.save(f"{recipe_name}_report.xlsx")

def on_calculate(button):
    recipe_name = app.getOptionBox("Рецепт")
    ingredients = get_recipe_ingredients(recipe_name)
    calories = calculate_calories(ingredients)
    cost = calculate_cost(ingredients)
    
    app.setLabel("calories", f"Энергетическая ценность: {calories} ккал")
    app.setLabel("cost", f"Стоимость: {cost} $")
    
    if button == "Сохранить в DOCX":
        save_to_docx(recipe_name, calories, cost)
    elif button == "Сохранить в XLSX":
        save_to_xlsx(recipe_name, calories, cost)

app = gui("Калькулятор рецептов", "400x300")

app.addLabel("title", "Выберите рецепт и рассчитайте его параметры")
app.addOptionBox("Рецепт", ["Вок", "Бургер", "Пицца"])

app.addButtons(["Рассчитать", "Сохранить в DOCX", "Сохранить в XLSX"], on_calculate)

app.addLabel("calories", "")
app.addLabel("cost", "")

app.go()