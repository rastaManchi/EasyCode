import sys
from PyQt6.QtWidgets import (QApplication,
                             QWidget,
                             QVBoxLayout,
                             QHBoxLayout,
                             QLabel,
                             QPushButton,
                             QLineEdit,
                             QTextEdit,
                             QListWidget,
                             QStackedWidget,
                             QMessageBox,
                             QListWidgetItem)
from PyQt6.QtCore import Qt


from db import *


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Библиотека рецептов")
window.resize(500, 400)

stack = QStackedWidget()
main_layout = QVBoxLayout()

window.setLayout(main_layout)
window.layout().addWidget(stack)

all_recipes_page = QWidget()
all_recipes_layout = QVBoxLayout()

recipe_list = QListWidget()
add_recipe_button = QPushButton("Добавить рецепт")

all_recipes_layout.addWidget(recipe_list)
all_recipes_layout.addWidget(add_recipe_button)

all_recipes_page.setLayout(all_recipes_layout)

window.show()
app.exec()
