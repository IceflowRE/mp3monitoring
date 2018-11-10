class Settings:
    def __init__(self):
        self.gui_update_time = 1
        self.check_update_at_startup = False

    def load(self, save_dict: dict):
        self.gui_update_time = save_dict.get("gui_update_time", 1)
        self.check_update_at_startup = save_dict.get("check_update_at_startup", False)

    def get_dict(self):
        return {
            "gui_update_time": self.gui_update_time,
            "check_update_at_startup": self.check_update_at_startup,
        }
