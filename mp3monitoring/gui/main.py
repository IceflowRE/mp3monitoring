from PyQt5.QtCore import QThread, Qt
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QAbstractItemView

import gui.menu_items as menu
from gui.data.data_table_model import DataTableModel
from gui.menu_items import file, help, settings
from gui.shutdown_overlay import ShutdownOverlay
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

        # shutdown overlay
        self.overlay = ShutdownOverlay(self)
        self.gridLayout.addWidget(self.overlay, 0, 0, 1, 1)
        self.overlay.hide()

        # init shutdown thread
        self.shutdown_worker = ShutdownWorker()
        self.shutdown_thread = QThread()
        self.shutdown_worker.status.connect(lambda msg: self.change_status_bar(msg))
        self.shutdown_worker.finished.connect(self.app.quit)
        self.shutdown_worker.moveToThread(self.shutdown_thread)
        self.shutdown_thread.started.connect(self.shutdown_worker.shutdown)

        #self.dataTree.setFocusPolicy(Qt.NoFocus)
        self.table_model = DataTableModel(['active', 'source', 'target', 'status'])
        self.update_data_table()

    def change_status_bar(self, msg, time=5000):
        self.statusBar.showMessage(msg, time)

    def closeEvent(self, event, close_immediately=False):  # TODO
        self.menuBar.setEnabled(False)
        self.overlay.show()

        self.shutdown_thread.start()

        event.ignore()

    def create_data_table(self):
        self.dataTableView.setModel(self.table_model)

    def update_data_table(self):
        """
        Updates the profile view content.
        :return:
        """
        pass
