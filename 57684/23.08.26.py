import sqlite3
# Импорт
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QListWidget, QStackedWidget, QMessageBox, QListWidgetItem
from PyQt6.QtCore import Qt




conn = sqlite3.connect("recipes.db")
cur = conn.cursor()


cur.execute("""
    CREATE TABLE IF NOT EXISTS recipes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        ingredients TEXT,
        steps TEXT
    )        
""")
conn.commit()


def load_recipes():
    # TODO: очистка списка рецептов
    cur.execute("SELECT id, name FROM recipes")
    for row in cur.fetchall():
        pass
        # TODO: добавление рецепта в список


def add_ingredient():
    name = None
    amount = None
    # TODO: Получить название ингредиента
    # TODO: Получить кол-во ингредиента

    if name and amount:
        #TODO: Добавление нового элемента в список
        #TODO: очистка поля для ввода названия
        #TODO: очистка поля для ввода кол-ва
        pass


def add_recipe(name, ingredients, steps):
    cur.execute("INSERT INTO recipes(name, ingredients, steps) VALUES (?, ?, ?)", [name, ingredients, steps])
    conn.commit()


# Создание основного окна
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Библиотека рецептов') # Заголовок окна
window.resize(500, 400) # Размер окна

# Подготовка
stack = QStackedWidget()
main_layout = QVBoxLayout()

# СТРАНИЦА "Все рецепты"
all_recipes_page = QWidget() # Создание страницы
all_recipes_layout = QVBoxLayout() # Создание вертикальной (основной) компоновки

# Виджеты страницы
recipe_list = QListWidget()
add_recipe_button = QPushButton("Добавить рецепт")

# Добавление виджетов на страницу
all_recipes_layout.addWidget(recipe_list)
all_recipes_layout.addWidget(add_recipe_button)

# Установка компановки
all_recipes_page.setLayout(all_recipes_layout)

# СТРАНИЦА "Добавление рецепта"
add_recipe_page = QWidget() # Создание страницы
add_recipe_layout = QVBoxLayout() # Создание вертикальной (основной) компоновки
ingredient_input_layout = QHBoxLayout() # Создание горизонтальной (второстепенной) компоновки

# Виджеты страницы
recipe_name_input = QLineEdit()
ingredient_name_input = QLineEdit()
ingredient_amount_input = QLineEdit()
add_ingredient_button = QPushButton("Добавить")
ingredients_list = QListWidget()
recipe_steps_input = QTextEdit()
save_button = QPushButton("Сохранить рецепт")
back_button = QPushButton("Назад к списку")

# Плейсхолдеры
recipe_name_input.setPlaceholderText("Название рецепта")
ingredient_name_input.setPlaceholderText("Ингредиент (например: Молоко)")
ingredient_amount_input.setPlaceholderText("Количество (например: 200 мл)")
recipe_steps_input.setPlaceholderText("Шаги приготовления")

# Добавление виджетов на страницу
add_recipe_layout.addWidget(recipe_name_input)
ingredient_input_layout.addWidget(ingredient_name_input)
ingredient_input_layout.addWidget(ingredient_amount_input)
ingredient_input_layout.addWidget(add_ingredient_button)
add_recipe_layout.addLayout(ingredient_input_layout) # Установка компановки
add_recipe_layout.addWidget(ingredients_list)
add_recipe_layout.addWidget(recipe_steps_input)
add_recipe_layout.addWidget(save_button)
add_recipe_layout.addWidget(back_button)

# Установка компановки
add_recipe_page.setLayout(add_recipe_layout)

# СТРАНИЦА "Просмотр рецепта"
view_recipe_page = QWidget() # Создание страницы
view_recipe_layout = QVBoxLayout() # Создание вертикальной компоновки

# Виджеты страницы
recipe_details_label = QLabel()
recipe_details_ingredients = QLabel()
recipe_details_steps = QLabel()
back_to_list_button = QPushButton("Назад к списку")

# Добавление виджетов на страницу
view_recipe_layout.addWidget(recipe_details_label)
view_recipe_layout.addWidget(recipe_details_ingredients)
view_recipe_layout.addWidget(recipe_details_steps)
view_recipe_layout.addWidget(back_to_list_button)

# Установка компановки
view_recipe_page.setLayout(view_recipe_layout)

#Добавляем страницы в стек
stack.addWidget(all_recipes_page)
stack.addWidget(add_recipe_page)
stack.addWidget(view_recipe_page)

# Установка компановки
window.setLayout(main_layout)

#Добавляем QStackedWidget на основную страницу
window.layout().addWidget(stack)

# Отображение окна
window.show()

# Запуск главного цикла приложения
app.exec()