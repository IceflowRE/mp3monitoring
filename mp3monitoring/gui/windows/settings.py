from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialogButtonBox, QMainWindow

from mp3monitoring.data.dynamic import config
from mp3monitoring.gui.windows.ui.settings import Ui_SettingsWindow


class SettingsWindow(QMainWindow, Ui_SettingsWindow):
    def __init__(self, parent):
        super(SettingsWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)

        self.set_item_actions()
        self.set_settings_values()

    def set_item_actions(self):
        self.dialogButtonBox.button(QDialogButtonBox.Apply).clicked.connect(self.apply_settings)
        self.dialogButtonBox.rejected.connect(self.close)

    def set_settings_values(self):
        self.guiUpdateTimeSpinBox.setValue(config.gui_update_time)
        self.checkForUpdatesBox.setChecked(config.check_update_at_startup)

    def apply_settings(self):
        config.gui_update_time = self.guiUpdateTimeSpinBox.value()
        config.check_update_at_startup = self.checkForUpdatesBox.isChecked()

        self.close()
