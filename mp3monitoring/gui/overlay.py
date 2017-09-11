import math
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush
from PyQt5.QtWidgets import QGridLayout, QLabel


class RotatingOverlay(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(RotatingOverlay, self).__init__(parent, flags=Qt.FramelessWindowHint)

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.fill_color = QtGui.QColor(30, 30, 30, 120)
        self.text_color = QtGui.QColor(255, 255, 255, 255)

        layout = QGridLayout(self)
        msg = QLabel("Shutting down...")
        msg.setStyleSheet('color: white')
        font = QtGui.QFont("Noto Sans UI", 16, QtGui.QFont.Bold)
        msg.setFont(font)
        layout.addWidget(msg, 0, 1)
        layout.setAlignment(QtCore.Qt.AlignHCenter)

    def paintEvent(self, event):
        size = self.size()
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing, True)

        # draw background
        painter.setPen(QtGui.QColor(255, 255, 255, 255))
        painter.setBrush(self.fill_color)
        painter.drawRect(0, 0, size.width(), size.height())

        """
        # draw waiting indicator
        for i in range(6):
            if (self.counter / 5) % 6 == i:
                painter.setBrush(QBrush(QtGui.QColor(127 + (self.counter % 5)*32, 127, 127)))
            else:
                painter.setBrush(QBrush(QtGui.QColor(127, 127, 127)))
            painter.drawEllipse(
                self.width()/2 + 30 * math.cos(2 * math.pi * i / 6.0) - 10,
                self.height()/2 + 30 * math.sin(2 * math.pi * i / 6.0) - 10,
                20, 20)
        """

        painter.end()
