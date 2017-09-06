from gui.menu_items.menu_item_file import MenuItemFile
from gui.menu_items.menu_item_help import MenuItemHelp
from gui.menu_items.menu_item_settings import MenuItemExtras
from gui.ui.main_window import Ui_MainWindow


class MainWindow(Ui_MainWindow):
    def __init__(self, window):
        Ui_MainWindow.__init__(self)
        self.setupUi(window)

        self.menuItemFile = MenuItemFile(self)  # init
        self.menuItemExtras = MenuItemExtras(self)  # init
        self.menuItemHelp = MenuItemHelp(self)  # init

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
