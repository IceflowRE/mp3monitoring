import json
from pathlib import Path

import mutagen.mp3

import data.dynamic
import data.settings
import data.static


def is_mp3(file_path: str):
    """
    Check a file for mp3 and if its a valid MPEG audio format.
    :param file_path: file to be checked
    :return: if its can be loaded as mp3 and if its a valid MPEG format.
    """
    try:
        return not mutagen.mp3.MP3(file_path).info.sketchy
    except mutagen.mp3.HeaderNotFoundError:
        pass
    except FileNotFoundError:
        pass
    return False


def get_all_files_after_time(directory, after_time=0):
    """
    Check all files in the given directory if access or creation time after the given time.
    :param directory: directory which will be checked
    :param after_time: time in seconds (unixtime)
    :return: list of modified/created files after time
    """
    files = directory.glob('**/*')
    return [file for file in files if
            (file.is_file() and (max(file.stat().st_mtime, file.stat().st_ctime) > after_time))]


def load_config_data(path: Path):
    """
    Loads the modification times from the save file.
    :param path:
    :return: JOB_DICT, dict[file, monitor]
    """
    with path.open('r', encoding='utf-8') as reader:
        save_dict = json.load(reader)
    return save_dict


def save_config_data(job_dict, path: Path):
    """
    Saves the modification times to the save file.
    :param job_dict: monitor jobs
    :param path:
    """
    json_dict = {'information': {'version': data.static.VERSION}, 'jobs': [], 'settings': {}}
    for job in job_dict.values():
        json_dict['jobs'].append(job.to_json_dict())

    json_dict['settings']['gui_update_time'] = data.settings.GUI_UPDATE_TIME
    json_dict['settings']['check_update_at_startup'] = False

    with path.open('w', encoding='utf-8') as writer:
        json.dump(json_dict, writer, indent=4)
