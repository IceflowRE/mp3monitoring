from functools import partial

from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QHeaderView, QMainWindow

from gui import monitor_table_view
from gui.check_box import CheckBoxDelegate
from gui.data.monitor_table_model import DataTableModel
from gui.widgets.shutdown_overlay import ShutdownOverlay
from gui.windows import menu_items
from gui.windows.ui.main import Ui_MainWindow
from gui.workers.shutdown_worker import ShutdownWorker


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.app = app

        menu_items.file.set_item_actions(self)
        menu_items.settings.set_item_actions(self)
        menu_items.help.set_item_actions(self)

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

        self.create_data_table()

        # add context menu to table view
        self.dataTableView.customContextMenuRequested.connect(
            partial(monitor_table_view.context_menu, self.dataTableView))

    def change_status_bar(self, msg, time=5000):
        self.statusBar.showMessage(msg, time)

    def closeEvent(self, event, close_immediately=False):  # TODO
        self.menuBar.setEnabled(False)
        self.overlay.show()

        self.shutdown_thread.start()

        event.ignore()

    def create_data_table(self):
        header = [' active ', ' source ', ' target ', ' status ', ' pause (s) ']
        table_model = DataTableModel(header, self)
        self.dataTableView.setModel(table_model)
        self.dataTableView.setSortingEnabled(False)  # TODO

        self.dataTableView.setItemDelegateForColumn(0, CheckBoxDelegate(self.dataTableView))

        h_header = self.dataTableView.horizontalHeader()
        h_header.setSectionResizeMode(0, QHeaderView.Fixed)  # active
        h_header.setSectionResizeMode(1, QHeaderView.Stretch)  # source dir
        h_header.setSectionResizeMode(2, QHeaderView.Stretch)  # target dir
        self.dataTableView.resizeColumnsToContents()
