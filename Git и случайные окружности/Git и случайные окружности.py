import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPen, QPainter, QColor
import random
from PyQt5.QtWidgets import *



class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.do_paint = False

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.btn = QPushButton('Рисовать', self)
        self.btn.resize(200, 40)
        self.btn.move(50, 250)
        self.btn.clicked.connect(self.push)

    def push(self):
        self.do_paint = True
        self.repaint()
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.ris(qp)
            qp.end()

    def ris(self, qp):
        qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        r = random.randint(5, 150)
        qp.drawEllipse(75, 75, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())