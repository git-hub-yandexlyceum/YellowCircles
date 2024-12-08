import sys
from random import randint

from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QPushButton, QMainWindow


class YellowCircles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.button: QPushButton = self.findChild(QPushButton, 'drawButton')
        self.button.clicked.connect(self.draw)

        self.circles: list[tuple[int, int, int]] = []

    def draw(self):
        self.circles = [
            (
                diameter := randint(10, 100),
                randint(0, self.width() - diameter),
                randint(0, self.height() - diameter)
            )
            for _ in range(randint(5, 30))]

        self.update()

    def paintEvent(self, event):
        drawer: QPainter = QPainter(self)
        drawer.setBrush(QColor(255, 255, 0))

        for (diameter, x, y) in self.circles:
            drawer.drawEllipse(x, y, diameter, diameter)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = YellowCircles()
    window.show()
    sys.exit(app.exec())
