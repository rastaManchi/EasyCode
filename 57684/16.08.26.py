import sys
from PyQt6.QtWidgets import QApplication, QGraphicsScene, QGraphicsView
from PyQt6.QtCore import Qt, QPointF
from PyQt6.QtGui import QPen, QBrush, QColor, QPolygonF, QPixmap
app = QApplication(sys.argv)
# Проверка наличия файла текстуры; если нет – создаём простую клетчатую текстуру
try:
    texture_pixmap = QPixmap("dots.png")
    if texture_pixmap.isNull():
        raise FileNotFoundError
except FileNotFoundError:
    # Создаём искусственную текстуру 20x20 с чередованием серых и белых квадратов
    texture_pixmap = QPixmap(20, 20)
    texture_pixmap.fill(Qt.GlobalColor.lightGray)
    from PyQt6.QtGui import QPainter
    painter = QPainter(texture_pixmap)
    painter.setPen(Qt.GlobalColor.black)
    painter.setBrush(Qt.GlobalColor.darkGray)
    painter.drawRect(0, 0, 10, 10)
    painter.drawRect(10, 10, 10, 10)
    painter.end()
# Создаём графическую сцену и устанавливаем её границы
scene = QGraphicsScene()
scene.setSceneRect(-400, -400, 800, 800)  # чтобы все фигуры поместились
# 1. Прямоугольник со штриховой красной обводкой (толщина 3) и голубой заливкой
pen_rect = QPen(QColor("red"), 3)
pen_rect.setStyle(Qt.PenStyle.DashLine)          # штриховая линия
brush_rect = QBrush(QColor("cyan"))
rect = scene.addRect(-350, -350, 150, 150, pen_rect, brush_rect)
# 2. Эллипс с синей сплошной обводкой (толщина 2) и заливкой жёлтым цветом
pen_ellipse = QPen(QColor("blue"), 2)
pen_ellipse.setStyle(Qt.PenStyle.SolidLine)      # можно не указывать, SolidLine по умолчанию
brush_ellipse = QBrush(QColor("yellow"))
ellipse = scene.addEllipse(100, -350, 120, 100, pen_ellipse, brush_ellipse)
# 3. Линия зелёного цвета толщиной 5 от точки (0,0) до (200,200)
pen_line = QPen(QColor("green"), 5)
# Линия не имеет заливки, поэтому brush не нужен
line = scene.addLine(-200, 100, 200, 300, pen_line)   # сместили, чтобы не накладывалась


# 4. Многоугольник (5 вершин) с обводкой чёрного цвета (толщина 2) и текстурной заливкой
pen_poly = QPen(QColor("black"), 2)
brush_poly = QBrush(texture_pixmap)   # текстурная кисть
points = [
    QPointF(200, 100),
    QPointF(320, 50),
    QPointF(380, 150),
    QPointF(270, 220),
    QPointF(150, 160)
]
polygon = QPolygonF(points)
poly = scene.addPolygon(polygon, pen_poly, brush_poly)
# 5. Изображение через QPixmap (файл image.jpg должен существовать, либо замените на свой)
try:
    image_pixmap = QPixmap("image.jpg")
    if image_pixmap.isNull():
        raise FileNotFoundError
except FileNotFoundError:
    # Если файла нет, создаём простой цветной квадрат с текстом
    image_pixmap = QPixmap(100, 100)
    image_pixmap.fill(Qt.GlobalColor.darkCyan)
    from PyQt6.QtGui import QPainter
    painter = QPainter(image_pixmap)
    painter.setPen(Qt.GlobalColor.white)
    painter.drawText(10, 50, "No image")
    painter.end()
# Масштабируем изображение до удобного размера (опционально)
image_pixmap = image_pixmap.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio)
pixmap_item = scene.addPixmap(image_pixmap)
pixmap_item.setPos(-300, 100)   # размещаем слева снизу
# Дополнительное задание: разрешить перетаскивание всех фигур
for item in (rect, ellipse, line, poly, pixmap_item):
    item.setFlag(item.GraphicsItemFlag.ItemIsMovable, True)
# Создаём представление и отображаем
view = QGraphicsView(scene)
view.setWindowTitle("Моя графическая композиция")
view.resize(800, 600)
view.show()
sys.exit(app.exec())
