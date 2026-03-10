# Импорты
import sys
from PyQt6.QtWidgets import *


# Создание окна
app = QApplication(sys.argv)
window = QWidget()

vbox = QVBoxLayout()
window.setLayout(vbox)

label = QLabel(text="Какой нибудь текст")
line_edit = QLineEdit()
button = QPushButton("OK")

vbox.addWidget(label)
vbox.addWidget(line_edit)
vbox.addWidget(button)



# Заголовок окна
window.setWindowTitle('Простое окно')


# Размер окна
window.resize(400, 300)


# Отображение окна
window.show()


# Цикл обработки событий
app.exec()
