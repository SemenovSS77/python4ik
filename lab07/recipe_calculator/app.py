import tkinter as tk
from tkinter import ttk, messagebox
from .managers import IngredientManager, RecipeManager
from .calculators import CaloriesCalculator, CostCalculator
from .reports import DocxReport, XlsxReport

class RecipeApp(tk.Tk):
    # Главный класс приложения
    def __init__(self):
        super().__init__()
        self.title("Калькулятор рецептов")
        self.geometry("400x300")
        
        # Инициализация компонентов
        self.ingredient_manager = IngredientManager()
        self.recipe_manager = RecipeManager()
        self.calories_calculator = CaloriesCalculator(self.ingredient_manager)
        self.cost_calculator = CostCalculator(self.ingredient_manager)
        self.docx_report = DocxReport()
        self.xlsx_report = XlsxReport()
        
        self.create_widgets()

    def create_widgets(self):
        # Создание интерфейса
        self.label_title = ttk.Label(self, text="Выберите рецепт и рассчитайте его параметры")
        self.label_title.pack(pady=10)
        
        self.recipe_var = tk.StringVar()
        self.combo_recipe = ttk.Combobox(
            self, 
            textvariable=self.recipe_var,
            values=list(self.recipe_manager.recipes.keys())
        )
        self.combo_recipe.pack(pady=5)
        
        self.btn_calculate = ttk.Button(self, text="Рассчитать", command=self.on_calculate)
        self.btn_calculate.pack(pady=5)
        
        self.btn_docx = ttk.Button(
            self, 
            text="Сохранить в DOCX", 
            command=lambda: self.on_save("docx")
        )
        self.btn_docx.pack(pady=5)
        
        self.btn_xlsx = ttk.Button(
            self, 
            text="Сохранить в XLSX", 
            command=lambda: self.on_save("xlsx")
        )
        self.btn_xlsx.pack(pady=5)
        
        self.label_calories = ttk.Label(self, text="")
        self.label_calories.pack(pady=5)
        
        self.label_cost = ttk.Label(self, text="")
        self.label_cost.pack(pady=5)

    def on_calculate(self):
        # Обработка расчета
        recipe_name = self.recipe_var.get()
        if not recipe_name:
            messagebox.showwarning("Ошибка", "Выберите рецепт")
            return
            
        ingredients = self.recipe_manager.recipes.get(recipe_name, {}).get("ingredients", {})
        calories = self.calories_calculator.calculate(ingredients)
        cost = self.cost_calculator.calculate(ingredients)
        
        self.label_calories.config(text=f"Энергетическая ценность: {calories:.2f} ккал")
        self.label_cost.config(text=f"Стоимость: {cost:.2f} $")

    def on_save(self, report_type):
        # Обработка сохранения отчета
        recipe_name = self.recipe_var.get()
        if not recipe_name:
            messagebox.showwarning("Ошибка", "Выберите рецепт")
            return
            
        ingredients = self.recipe_manager.recipes.get(recipe_name, {}).get("ingredients", {})
        calories = self.calories_calculator.calculate(ingredients)
        cost = self.cost_calculator.calculate(ingredients)
        
        if report_type == "docx":
            success = self.docx_report.save(recipe_name, calories, cost)
        else:
            success = self.xlsx_report.save(recipe_name, calories, cost)
            
        if success:
            messagebox.showinfo("Успех", f"Отчет сохранен как {recipe_name}_report.{report_type}")


if __name__ == "__main__":
    app = RecipeApp()
    app.mainloop()