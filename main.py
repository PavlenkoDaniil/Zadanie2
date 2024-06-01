from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
import sys
import random
from UI import Ui_MainWindow

class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.draw)
        self.circle_x = None
        self.circle_y = None
        self.circle_size = None

    def draw(self):
        self.circle_x = 150
        self.circle_y = 150
        self.circle_size = 40
        self.update()

    def paintEvent(self, event):
        if self.circle_x is not None and self.circle_y is not None and self.circle_size is not None:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(255, 255, 0))  # жёлтый цвет
            qp.setBrush(QColor(255, 255, 0))  # жёлтый цвет
            qp.drawEllipse(self.circle_x, self.circle_y, self.circle_size, self.circle_size)
            qp.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
