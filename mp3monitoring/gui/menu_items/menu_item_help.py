from gui import dialogs


class MenuItemHelp:
    def __init__(self, parent):
        self.parent = parent
        self.set_item_actions()

    def set_item_actions(self):
        # Help -> Help
        self.parent.action_help.triggered.connect(self.handle_help_help)
        # Help -> Check for udpates
        self.parent.action_check_for_updates.triggered.connect(self.handle_help_check_updates)
        # Help -> About
        self.parent.action_about.triggered.connect(self.handle_help_about)

    def handle_help_help(self):
        dialogs.information_dialog('Not implemented yet.', 'Help is not implemented yet.')

    def handle_help_check_updates(self):
        dialogs.information_dialog('Not implemented yet.', 'Checking for updates is not implemented yet.')

    def handle_help_about(self):
        dialogs.information_dialog('Not implemented yet.', 'About is not implemented yet.')
