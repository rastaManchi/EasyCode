# Импорты
import sys
from PyQt6.QtWidgets import *


# Инициализация приложения
app = QApplication(sys.argv)


# Создание окна
window = QWidget()
window.setWindowTitle("Главное окно")
secondary_window = QWidget()


# Создание дополнительного окна
def open_secondary_window():
    secondary_window.setWindowTitle("Вторичное окно")
    secondary_label = QLabel("Это вторичное окно!")
    secondary_vbox = QVBoxLayout()
    secondary_vbox.addWidget(secondary_label)
    secondary_window.setLayout(secondary_vbox)
    secondary_window.show()


# Кнопка для открытия второго окна
button_open_secondary = QPushButton("Открыть второе окно")


# Привязываем сигнал нажатия кнопки к открытию окна
button_open_secondary.clicked.connect(open_secondary_window)


# Компоновка основного окна
vbox = QVBoxLayout()
vbox.addWidget(button_open_secondary)
window.setLayout(vbox)


# Показываем главное окно
window.show()


# Цикл обработки событий
app.exec()
