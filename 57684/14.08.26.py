# Импорты
import sys
from PyQt6.QtWidgets import *


calc_struct = [
    ['ce', 'c', 'del', '/'],
    ['7', '8', '9', 'x'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['+_', '0', ',', '=']
]


# Создание окна
app = QApplication(sys.argv)
window = QWidget()


# Заголовок окна
window.setWindowTitle('Простое окно')


# Размер окна
window.resize(400, 300)

text = QLabel('привет')
text.move(50, 50)

# Отображение окна
window.show()


# Цикл обработки событий
app.exec()
