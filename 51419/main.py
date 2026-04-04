import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

count = 0
def add_click():
    global count
    count += 1
    label.setText(f"Радость котика: {count}")

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Calc Click")
window.resize(300, 200)

label = QLabel("Радость котика: 0")
button = QPushButton("Погладь кота")
button.clicked.connect(add_click)

layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(button)

window.setLayout(layout)

window.show()
sys.exit(app.exec())