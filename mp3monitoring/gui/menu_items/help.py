from functools import partial

import gui.dialogs
from gui.about import AboutWindow


def set_item_actions(parent):
    # Help -> Help
    parent.action_help.triggered.connect(handle_help_help)
    # Help -> Check for udpates
    parent.action_check_for_updates.triggered.connect(handle_help_check_updates)
    # Help -> About
    parent.action_about.triggered.connect(partial(handle_help_about, parent))


def handle_help_help():
    gui.dialogs.information_dialog('Not implemented yet.', 'Help is not implemented yet.')


def handle_help_check_updates():
    gui.dialogs.information_dialog('Not implemented yet.', 'Checking for updates is not implemented yet.')


def handle_help_about(parent):
    ab = AboutWindow(parent)
    ab.show()
    #dialogs.information_dialog('Not implemented yet.', 'About is not implemented yet.')
