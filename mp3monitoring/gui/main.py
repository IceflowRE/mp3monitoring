import threading

import time
from functools import partial

from PyQt5.QtCore import Qt, QThread, QObject, pyqtSignal, pyqtSlot, QCoreApplication
from PyQt5.QtWidgets import QMainWindow

import core
import gui.menu_items as menu
from gui.menu_items import file, help, settings
from gui.shutdown_worker import ShutdownWorker
from gui.ui.main import Ui_MainWindow
from gui.overlay import RotatingOverlay


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.app = app

        menu.file.set_item_actions(self)
        menu.settings.set_item_actions(self)
        menu.help.set_item_actions(self)

        #self.update_offline_profile_content()

    def closeEvent(self, event):  # TODO
        self.statusBar.showMessage('Shutting down...', 5000)

        overlay = RotatingOverlay(parent=self.centralWidget)
        self.gridLayout.addWidget(overlay, 0, 0, 1, 1)
        overlay.resize(self.size())
        overlay.show()

        self.shutdown_worker = ShutdownWorker()
        self.thread = QThread()
        self.shutdown_worker.status.connect(lambda s: print(s))
        # 3 - Move the Worker object to the Thread object
        self.shutdown_worker.moveToThread(self.thread)
        # 5 - Connect Thread started signal to Worker operational slot method
        self.thread.started.connect(self.shutdown_worker.shutdown)
        # * - Thread finished signal will close the app if you want!
        #self.thread.finished.connect(self.app.exit)
        # 6 - Start the thread
        self.thread.start()

        # TODO splash screen shutdown
        #event.accept()
        event.ignore()

    def update_offline_profile_content(self):
        """
        Updates the profile view content.
        :return:
        """
        pass
        """
        self.profileTree.clear()
        for nick_name, cur_offline_profile in DataCont.offline_profile.items():
            tree_item = QTreeWidgetItem(self.profileTree)
            font = QFont()
            font.setWeight(QFont.Bold)
            tree_item.setFont(0, font)
            tree_item.setText(0, nick_name)
            for cur_ghost in cur_offline_profile.ghosts_dict.values():
                child_item = QTreeWidgetItem(tree_item)
                child_item.setText(1, GhostTrack[cur_ghost.track].value)
                child_item.setText(2, GhostWeather[cur_ghost.weather].value)
        self.profileTree.expandToDepth(0)
        """
