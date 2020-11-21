import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPen, QPainter, QColor
from PyQt5.QtWidgets import QColorDialog
import random


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.push)
        self.do_paint = False

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
        qp.setBrush(QColor(255, 251, 56))
        r = random.randint(5, 150)
        qp.drawEllipse(75, 75, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())