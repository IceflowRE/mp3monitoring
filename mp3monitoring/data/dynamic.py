"""
Data which will be generated while starting and should be available global.
"""
from pathlib import Path

import mp3monitoring.data.static as static_data
from mp3monitoring.data.settings import Settings

#: config file
save_file = Path.home().joinpath('.' + static_data.NAME).joinpath('data.sav')
#: job dictionary of active and not active monitoring jobs
job_dict = {}
#: option to disable tqdm output
disable_tqdm = False

config = Settings()
