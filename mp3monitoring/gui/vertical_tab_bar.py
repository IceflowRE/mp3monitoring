from PySide6.QtCore import Qt
from PySide6.QtGui import QPaintEvent
from PySide6.QtWidgets import QStyle, QStyleOptionTab, QTabBar, QStylePainter, QTabWidget


class VerticalTabBar(QTabBar):
    """
    Vertical tab bar.
    """
    def paintEvent(self, event: QPaintEvent):
        painter = QStylePainter(self)
        option = QStyleOptionTab()
        for index in range(self.count()):
            self.initStyleOption(option, index)
            painter.drawControl(QStyle.CE_TabBarTabShape, option)
            painter.drawText(self.tabRect(index), Qt.AlignCenter | Qt.TextDontClip, self.tabText(index))

    def tabSizeHint(self, index):
        size = super().tabSizeHint(index)
        if size.width() < size.height():
            size.transpose()
        return size


class VerticalTabWidget(QTabWidget):
    """
    Widget for the vertical tab bar.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTabBar(VerticalTabBar())
