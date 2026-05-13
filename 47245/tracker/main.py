# Импорт
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QProgressBar
from PyQt6.QtCore import Qt


def update_display():
    procent = min(int(total_water / goal * 100), 100)
    progress_bar.setValue(procent)
    total_label.setText(f"Выпито сегодня: {total_water} / {goal} мл")
    
    
def add_water():
    global total_water
    amount = int(water_input.text())
    
    if amount > 0:
        total_water += amount
        water_input.clear()
        update_display()
        
        
def set_goal():
    global goal
    new_goal = int(goal_input.text())
    
    if new_goal > 0:
        goal = new_goal
        goal_input.clear()
        update_display()
        

def reset():
    global goal, total_water
    goal = 2000
    total_water = 0
    update_display()


# Переменные
goal = 2000  # Цель по умолчанию
total_water = 0 # Количество выпитой воды
new_goal = 0 # Новая цель


# Создание основного окна
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Трекер выпитой воды') # Заголовок окна
window.resize(400, 300) # Размер окна


# Основная компоновка
layout = QVBoxLayout() # Создание компоновки
window.setLayout(layout) # Установка компоновки


# Второстепенная компоновка
goal_layout = QHBoxLayout() # Создание компоновки
layout.addLayout(goal_layout) # Установка компоновки


# Второстепенная компоновка
input_layout = QHBoxLayout() # Создание компоновки


# Создание компонентов
title_label = QLabel("Введите объем воды (мл):")
total_label = QLabel(f"Выпито сегодня: {total_water} / {goal} мл")
goal_input = QLineEdit()
water_input = QLineEdit()

set_goal_button = QPushButton("Задать цель")
set_goal_button.clicked.connect(set_goal)

add_button = QPushButton("Добавить")
add_button.clicked.connect(add_water)

reset_button = QPushButton("Сбросить статистику")
reset_button.clicked.connect(reset)

progress_bar = QProgressBar()


# Установка плейсхолдера
goal_input.setPlaceholderText("Цель в мл (по умолчанию: 2000)")
water_input.setPlaceholderText("Например: 200")


# Добавляем виджеты в компоновку
layout.addWidget(title_label)
layout.addLayout(input_layout) # Установка компоновки
goal_layout.addWidget(goal_input)
goal_layout.addWidget(set_goal_button)
input_layout.addWidget(water_input)
input_layout.addWidget(add_button)
layout.addWidget(progress_bar)
layout.addWidget(total_label)
layout.addWidget(reset_button)


# Отображение окна
window.show()


# Запуск главного цикла приложения
app.exec()
