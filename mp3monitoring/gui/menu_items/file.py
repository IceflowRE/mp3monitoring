from PyQt5.QtWidgets import QFileDialog


def set_item_actions(parent):
    # File -> Add...
    parent.actionAdd.triggered.connect(handle_file_add)
    # File -> Exit
    parent.actionExit.triggered.connect(parent.close)


def handle_file_add():
    """
    Can load ONLY offline profiles at the moment.
    :return:
    """
    source_dir = QFileDialog.getExistingDirectory(None, 'Select a source directory', options=QFileDialog.ShowDirsOnly)
    target_dir = QFileDialog.getExistingDirectory(None, 'Select a target directory', options=QFileDialog.ShowDirsOnly)
