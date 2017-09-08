"""
Data which will be generated while starting and should be available global.
"""
from pathlib import Path

from data import static

SAVE_FILE = Path.home().joinpath('.' + static.NAME.replace(' ', '_')).joinpath('last_mod_times.sav')
