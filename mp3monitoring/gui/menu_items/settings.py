import gui.dialogs


def set_item_actions(parent):
    parent.actionSettings.triggered.connect(handle_settings_settings)


def handle_settings_settings():
    gui.dialogs.information_dialog('Not implemented yet.', 'Help is not implemented yet.')
