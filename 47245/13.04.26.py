# Импорты
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt


# Инициализация приложения
app = QApplication(sys.argv)


# Создание окна
window = QWidget()
window.setWindowTitle("Пример вкладок")


def handle2(event):
    if event.key() == Qt.Key.Key_Space:
        print('Пробел отжат')
        
        
def handle(event):
    if event.key() == Qt.Key.Key_Space:
        print('Пробел нажат')
        
        
def handle3(event):
    if event.button() == Qt.MouseButton.LeftButton:
        print('Левая кнопка мыши нажата')
        
def handle4(event):
    if event.button() == Qt.MouseButton.LeftButton:
        print('Левая кнопка мыши отжата')
        
def handle5(event):
    print(event.position().x(), event.position().y())

window.keyPressEvent = handle
window.keyReleaseEvent = handle2
window.mousePressEvent = handle3
window.mouseReleaseEvent = handle4
window.mouseMoveEvent = handle5

# Показываем окно
window.show()


# Цикл обработки событий
app.exec()