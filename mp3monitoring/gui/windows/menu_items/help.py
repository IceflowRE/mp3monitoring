from functools import partial

import gui.widgets.dialogs
from gui.windows.about import AboutWindow


def set_item_actions(parent):
    # Help -> Help
    parent.actionHelp.triggered.connect(handle_help_help)
    # Help -> Check for udpates
    parent.actionCheckForUpdates.triggered.connect(handle_help_check_updates)
    # Help -> About
    parent.actionAbout.triggered.connect(partial(handle_help_about, parent))


def handle_help_help():
    gui.widgets.dialogs.information_dialog('Not implemented yet.', 'Help is not implemented yet.')


def handle_help_check_updates():
    gui.widgets.dialogs.information_dialog('Not implemented yet.', 'Checking for updates is not implemented yet.')


def handle_help_about(parent):
    ab = AboutWindow(parent)
    ab.show()
