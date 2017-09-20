from functools import partial

from PyQt5.QtCore import QThread
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QDialogButtonBox, QHeaderView, QMainWindow, QMenu, QSystemTrayIcon

from gui.check_box import CheckBoxDelegate
from gui.data import monitor_table_view
from gui.data.monitor_table_model import DataTableModel
from gui.widgets import dialogs
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

        # tray icon
        self.tray_icon = None
        self.create_tray_icon()

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
        event.ignore()
        if not QSystemTrayIcon.isSystemTrayAvailable():
            value = dialogs.question_dialog('Exiting...', 'Do you really want to exit?')
            if bool(value & QDialogButtonBox.Yes):
                self.exit()
        else:
            self.tray_icon.show()
            self.hide()
            if QSystemTrayIcon.supportsMessages():  # TODO: seems not to work, on at least win10
                self.tray_icon.showMessage("MP3 Monitoring is running in background!",
                                           "Double click tray icon to open window and right click for menu.")

    def exit(self):  # TODO: deactivate close button
        self.menuBar.setEnabled(False)
        self.overlay.show()
        self.show_window()

        self.shutdown_thread.start()

    def create_tray_icon(self):
        icon = QIcon()
        icon.addPixmap(QPixmap("../data/icon_export.svg"), QIcon.Normal, QIcon.Off)
        self.tray_icon = QSystemTrayIcon(icon)
        self.tray_icon.activated.connect(self.tray_icon_clicked)

        menu = QMenu(self)
        open_action = menu.addAction("Open")
        menu.addSeparator()
        exit_action = menu.addAction("Exit")
        open_action.triggered.connect(self.show_window)
        exit_action.triggered.connect(self.exit)
        self.tray_icon.setContextMenu(menu)

    def tray_icon_clicked(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            self.show_window()
        elif reason == QSystemTrayIcon.Context:
            pass  # context menu automatically shown by the system tray icon

    def show_window(self):
        self.show()
        self.tray_icon.hide()

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
