from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow

import core
import gui.menu_items as menu
from gui.menu_items import file, help, settings
from gui.ui.main import Ui_MainWindow
from gui.waiting_indicator import WaitingOverlay


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        menu.file.set_item_actions(self)
        menu.settings.set_item_actions(self)
        menu.help.set_item_actions(self)

        #self.update_offline_profile_content()

    def closeEvent(self, event):  # TODO
        self.statusBar.showMessage('Shutting down...', 5000)

        overlay = WaitingOverlay(parent=self.centralWidget)
        overlay.resize(self.size())
        overlay.show()
        core.shutdown()

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
