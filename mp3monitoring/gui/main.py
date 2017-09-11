from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QMainWindow

import gui.menu_items as menu
from gui.menu_items import file, help, settings
from gui.overlay import RotatingOverlay
from gui.shutdown_worker import ShutdownWorker
from gui.ui.main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.app = app

        menu.file.set_item_actions(self)
        menu.settings.set_item_actions(self)
        menu.help.set_item_actions(self)

        # init shutdown thread
        self.shutdown_worker = ShutdownWorker()
        self.shutdown_thread = QThread()
        self.shutdown_worker.status.connect(lambda msg: self.change_status_bar(msg))
        self.shutdown_worker.finished.connect(self.app.quit)
        self.shutdown_worker.moveToThread(self.shutdown_thread)
        self.shutdown_thread.started.connect(self.shutdown_worker.shutdown)

        #self.update_offline_profile_content()

    def change_status_bar(self, msg, time=5000):
        self.statusBar.showMessage(msg, time)

    def closeEvent(self, event, close_immediately=False):  # TODO
        overlay = RotatingOverlay(parent=self)
        self.gridLayout.addWidget(overlay, 0, 0, 1, 1)
        overlay.show()

        self.shutdown_thread.start()

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
