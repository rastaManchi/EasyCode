# Импорты
import sys
from PyQt6.QtWidgets import *


# Инициализация приложения
app = QApplication(sys.argv)


# Создание окна
window = QWidget()
window.setWindowTitle("Пример вкладок")




# Создаем таббар
dfsdjkfsdf = QToolBox()


# Основная компоновка
vbox = QVBoxLayout()


# Устанавливаем компоновку в окно
window.setLayout(vbox)


# Добавляем tabbar в компоновку
vbox.addWidget(dfsdjkfsdf)


# Первая вкладка (домашняя страница)
home_tab = QWidget()
home_label = QLabel("Домашняя страница")
home_vbox = QVBoxLayout()
home_vbox.addWidget(home_label)
home_tab.setLayout(home_vbox)


# Вторая вкладка (контакты)
contacts_tab = QWidget()
contacts_label = QLabel("Список контактов")
contacts_vbox = QVBoxLayout()
contacts_vbox.addWidget(contacts_label)
contacts_tab.setLayout(contacts_vbox)


# Третья вкладка (настройки)
settings_tab = QWidget()
settings_label = QLabel("Настройки профиля")
settings_vbox = QVBoxLayout()
settings_vbox.addWidget(settings_label)
settings_tab.setLayout(settings_vbox)


# Добавляем вкладки в tabbar
dfsdjkfsdf.addItem(home_tab, "Главная")
dfsdjkfsdf.addItem(contacts_tab, "Контакты")
dfsdjkfsdf.addItem(settings_tab, "Настройки")


# Показываем окно
window.show()


# Цикл обработки событий
app.exec()
