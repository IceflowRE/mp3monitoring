from PyQt5.QtCore import Qt
from PyQt5.QtSvg import QGraphicsSvgItem
from PyQt5.QtWidgets import QGraphicsScene, QMainWindow

from data import static
from gui.ui.about import Ui_AboutWindow


class AboutWindow(QMainWindow, Ui_AboutWindow):
    def __init__(self, parent):
        super(AboutWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        #self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setFixedSize(self.size())
        self.closeButton.clicked.connect(self.close)

        # set window background
        self.setStyleSheet('background: palette(Base)')

        # set descriptions
        self.programName.setText(static.NAME)
        self.version.setText(static.VERSION)
        self.authorValue.setText("<a href=\"{link}\">{name}</a>".format(link=static.AUTHOR_GITHUB, name=static.AUTHOR))
        self.licenseValue.setText("<a href=\"https://www.gnu.org/licenses/gpl-3.0-standalone.html\">GPLv3</a>")

        # set logo
        self.logo.setStyleSheet('background: transparent')
        scene = QGraphicsScene()
        svg = QGraphicsSvgItem('../data/icon_export.svg')
        svg.setScale(160 / svg.boundingRect().width())
        scene.addItem(svg)
        self.logo.setScene(scene)