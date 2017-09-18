import json
from pathlib import Path

import mutagen.mp3

from data import dynamic, static


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


def init_monitor_dir(source_dir, target_dir):
    """
    Check source and initialize target directory.
    :param source_dir: source directory
    :param target_dir: mp3 target folder
    """
    if not source_dir.exists() or not source_dir.is_dir():
        raise FileNotFoundError

    if not target_dir.exists():
        Path.mkdir(target_dir, parents=True)
    elif not target_dir.is_dir():
        raise NotADirectoryError


def load_config_data():
    """
    Loads the modification times from the save file.
    :return: job_dict, dict[file, monitor]
    """
    save_dict = {}
    with dynamic.SAVE_FILE.open('r', encoding='utf-8') as reader:
        save_dict = json.load(reader)
    return save_dict


def save_config_data(job_dict):
    """
    Saves the modification times to the save file.
    :param job_dict: monitor jobs
    """
    json_dict = {}
    json_dict['information'] = {'version': static.VERSION}
    json_dict['jobs'] = []
    for job in job_dict:
        json_dict['jobs'].append(job.to_json_dict())
    with dynamic.SAVE_FILE.open('w', encoding='utf-8') as writer:
        json.dump(json_dict, writer, indent=4)
