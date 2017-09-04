from pathlib import Path

VERSION = '1.0.0'
NAME = 'MP3 Monitoring'
AUTHOR = 'Iceflower S'
AUTHOR_EMAIL = 'iceflower@gmx.de'

SAVE_FILE = Path.home().joinpath('.' + NAME.replace(' ', '_')).joinpath('last_mod_times.sav')
