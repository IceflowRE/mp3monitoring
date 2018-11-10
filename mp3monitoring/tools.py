import json
from pathlib import Path

import mp3monitoring.data.settings as settings_data
import mp3monitoring.data.static as static_data
from mp3monitoring.data.dynamic import config


def load_save_file(path: Path):
    """
    Loads the modification times from the save file.
    :param path:
    :return: JOB_DICT, dict[file, monitor]
    """
    with path.open('r', encoding='utf-8') as reader:
        save_dict = json.load(reader)
    return save_dict


def save_save_file(job_dict, path: Path):
    """
    Saves the modification times to the save file.
    :param job_dict: monitor jobs
    :param path:
    """
    json_dict = {'information': {'version': static_data.VERSION}, 'jobs': [], 'settings': {}}
    for job in job_dict.values():
        json_dict['jobs'].append(job.to_json_dict())

    json_dict['settings'] = config.get_dict()

    with path.open('w', encoding='utf-8') as writer:
        json.dump(json_dict, writer, indent=4)
