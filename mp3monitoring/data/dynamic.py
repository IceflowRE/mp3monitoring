"""
Data which will be generated while starting and should be available global.
"""
from pathlib import Path

import data.static

SAVE_FILE = Path.home().joinpath('.' + data.static.NAME.replace(' ', '_')).joinpath('data.sav')

JOB_DICT = {}

GUI_UPDATE_TIME = 1000
CHECK_UPDATE_AT_STARTUP = False
