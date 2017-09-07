from PyQt5.QtWidgets import QMainWindow

import gui.menu_items as menu
from gui.menu_items import file, settings, help
from gui.ui.main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        menu.file.set_item_actions(self)
        menu.settings.set_item_actions(self)
        menu.help.set_item_actions(self)

        #self.update_offline_profile_content()

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
