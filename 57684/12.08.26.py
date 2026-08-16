# Импорты
import sys
from PyQt6.QtWidgets import *


# Создание окна
app = QApplication(sys.argv)
window = QWidget()


# Заголовок окна
window.setWindowTitle('Простое окно')


# Размер окна
window.resize(400, 300)


# Создаем контейнер
vbox = QVBoxLayout()
window.setLayout(vbox)


# Создаем текстовую метку
label = QLabel("Привет, мир!")
label.setStyleSheet( # Задаем стили
    "color: #ff5733;"              # оранжевый цвет текста
    "font-size: 18px;"             # крупный шрифт
    "font-weight: bold;"           # полужирный шрифт
)


# Создаем поле для ввода
input_field = QLineEdit()
input_field.setStyleSheet( # Задаем стили
    "background-color: #fafafa;"   # светло-серый фон
    "border: 2px solid #cacaca;"   # тонкая светлая рамка
    "padding: 5px;"                # внутренние отступы
    "border-radius: 5px;"          # скругленные углы
)


# Создаем кнопку
button = QPushButton("OK")
button.setStyleSheet( # Задаем стили
    "background-color: #4CAF50;"   # зеленый фон
    "color: white;"                 # белый текст
    "border: none;"                 # убрать границу
    "padding: 10px 20px;"          # внешние отступы
    "font-size: 16px;"             # увеличенный шрифт
    "border-radius: 5px;"          # скругленные углы
)


vbox.addWidget(label) # Добавляем метку в контейнер
vbox.addWidget(input_field) # Добавляем поле для ввода в контейнер
vbox.addWidget(button) # Добавляем кнопку в контейнер


# Отображение окна
window.show()


# Цикл обработки событий
app.exec()
