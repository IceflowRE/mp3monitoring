from PyQt5.QtWidgets import QFileDialog

from gui import dialogs


def set_item_actions(parent):
    # File -> Add...
    parent.action_add.triggered.connect(handle_file_add)
    # File -> Exit
    parent.action_exit.triggered.connect(handle_file_exit)


def handle_file_add():
    """
    Can load ONLY offline profiles at the moment.
    :return:
    """
    directory = QFileDialog.getExistingDirectory(None, 'Select directory', options=QFileDialog.ShowDirsOnly)


def handle_file_exit():
    dialogs.information_dialog('Not implemented yet.', 'Exit is not implemented yet.')

"""
reply = Dialogs.question_dialog('File changed...', 'Do you want to save the file?')

if reply == QMessageBox.Yes:
    # DataContainer.save_offline_profiles()
    Dialogs.information_dialog('Not implemented yet.', 'Saving files is not implemented yet.')
elif reply == QMessageBox.No:
    pass
elif reply == QMessageBox.Cancel:
    return  # nothing to do
else:
    print('Unexpected input: ' + str(reply))
    return
if DataCont.load_offline_profiles_from_file(filename):
    self.parent.update_offline_profile_content()
    self.parent.statusBar.showMessage('Loaded: ' + filename, 5000)
else:
    self.parent.statusBar.showMessage('Loading failed: ' + filename, 5000)
"""
