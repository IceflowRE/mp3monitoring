"""
Data which will be generated while starting and should be available global.
"""
from pathlib import Path

import mp3monitoring.data.static as static_data

#: config file
SAVE_FILE = Path.home().joinpath('.' + static_data.NAME).joinpath('data.sav')
#: job dictionary of active and not active monitoring jobs
JOB_DICT = {}
#: option to disable tqdm output
DISABLE_TQDM = False
