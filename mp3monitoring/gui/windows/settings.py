from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QDialogButtonBox

import data.settings
from gui.windows.ui.settings import Ui_SettingsWindow


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
        self.guiUpdateTimeSpinBox.setValue(data.settings.GUI_UPDATE_TIME)
        self.checkForUpdatesBox.setChecked(data.settings.CHECK_UPDATE_AT_STARTUP)

    def apply_settings(self):
        data.settings.GUI_UPDATE_TIME = self.guiUpdateTimeSpinBox.value()
        data.settings.CHECK_UPDATE_AT_STARTUP = self.checkForUpdatesBox.isChecked()

        self.close()
