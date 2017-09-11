from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class RotatingOverlay(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(RotatingOverlay, self).__init__(parent, flags=Qt.FramelessWindowHint)

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.fill_color = QtGui.QColor(30, 30, 30, 120)
        self.text_color = QtGui.QColor(255, 255, 255, 255)

    def paintEvent(self, event):
        # get current window size
        size = self.size()
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setRenderHint(QtGui.QPainter.Antialiasing, True)
        qp.setPen(self.fill_color)
        qp.setBrush(self.fill_color)
        qp.drawRect(0, 0, size.width(), size.height())

        font = QtGui.QFont()
        font.setPixelSize(18)
        font.setBold(True)
        qp.setFont(font)
        qp.setPen(self.text_color)
        ow = int(size.width() / 2)
        oh = int(size.height() / 2)
        qp.drawText(ow, oh, "Yep, I'm a pop up.")

        qp.end()
