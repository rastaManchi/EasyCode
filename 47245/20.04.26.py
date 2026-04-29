# Импорты
import sys
from PyQt6.QtWidgets import QApplication, QGraphicsScene, QGraphicsView
from PyQt6.QtCore import Qt, QPointF
from PyQt6.QtGui import QPen, QBrush, QColor, QPolygonF
# Инициализация приложения
app = QApplication(sys.argv)
# Создаем графическую сцену
scene = QGraphicsScene()
# --- Прямоугольник ---
rect_item = scene.addRect(
    -50, -50,            # координаты верхнего левого угла
    100, 100,            # ширина и высота
    pen=QPen(QColor("black"), 2),
    brush=QBrush(QColor("green"))
)
rect_item.setFlag(rect_item.GraphicsItemFlag.ItemIsMovable, True)
# --- Эллипс ---
ellipse_item = scene.addEllipse(
    100, -50,            # координаты центра (на самом деле top-left, но для эллипса это bounding rect)
    100, 100,            # горизонтальный и вертикальный диаметры
    pen=QPen(QColor("black"), 2),
    brush=QBrush(QColor("yellow"))
)
ellipse_item.setFlag(ellipse_item.GraphicsItemFlag.ItemIsMovable, True)
# --- Линия ---
line_item = scene.addLine(
    -50, 50,             # начальная точка
    150, 50,             # конечная точка
    pen=QPen(QColor("red"), 3)
)
# --- Многоугольник (треугольник) ---
points_list = [
    QPointF(250, -50),
    QPointF(200, 50),
    QPointF(300, 50)
]
polygon = QPolygonF(points_list)
poly_item = scene.addPolygon(
    polygon,
    pen=QPen(QColor("black"), 2),
    brush=QBrush(QColor("cyan"))
)
# Создаем виджет для отображения сцены
view = QGraphicsView(scene)
view.setWindowTitle("Фигуры в PyQt")
view.resize(600, 400)
view.show()
# Цикл обработки событий
app.exec()
