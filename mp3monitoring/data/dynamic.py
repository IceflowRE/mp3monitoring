"""
Data which will be generated while starting and should be available global.
"""
from pathlib import Path

from data import static

SAVE_FILE = Path.home().joinpath('.' + static.NAME.replace(' ', '_')).joinpath('data.sav')

GUI_UPDATE_TIME = 1000
CHECK_UPDATE_AT_STARTUP = False
