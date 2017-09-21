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


def load_settings(save_dict):
    if 'settings' in save_dict:
        settings = save_dict['settings']
        for value in data.static.SETTINGS_VALUES:
            if value.lower() in settings:
                setattr(data.settings, value, settings[value.lower()])
            else:
                print('{value} not found in settings.'.format(value=value))
    else:
        print('No settings found in save file.')


def load_save_file(path: Path):
    """
    Loads the modification times from the save file.
    :param path:
    :return: JOB_DICT, dict[file, monitor]
    """
    with path.open('r', encoding='utf-8') as reader:
        save_dict = json.load(reader)
    return save_dict


def get_settings_dict():
    settings = {}
    for value in data.static.SETTINGS_VALUES:
        try:
            settings[value.lower()] = getattr(data.settings, value)
        except AttributeError:
            print('Internal fail, for settings variables. ({variable}'.format(variable=value))
    return settings


def save_save_file(job_dict, path: Path):
    """
    Saves the modification times to the save file.
    :param job_dict: monitor jobs
    :param path:
    """
    json_dict = {'information': {'version': data.static.VERSION}, 'jobs': [], 'settings': {}}
    for job in job_dict.values():
        json_dict['jobs'].append(job.to_json_dict())

    json_dict['settings'] = get_settings_dict()

    with path.open('w', encoding='utf-8') as writer:
        json.dump(json_dict, writer, indent=4)
