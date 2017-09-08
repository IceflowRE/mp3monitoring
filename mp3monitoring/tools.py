from pathlib import Path

import mutagen.mp3

import static_data


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


def load_config_data():
    """
    Loads the modification times from the save file.
    :return: modification dict, dict[file, mod_time]
    """
    save_dict = {}
    with static_data.SAVE_FILE.open('r', encoding='utf-8') as reader:
        lines = reader.readlines()
        lines = [line.rstrip() for line in lines]
        it = iter(lines)
        next(it)  # skip version value, not used until now
        for line in it:
            try:
                # resolve, due to fixing possibly manually changed values
                save_dict[str(Path(line).resolve())] = float(next(it))
            except StopIteration:
                print('Save file is corrupted. Could not load everything.')
    return save_dict


def save_config_data(mod_time_dict):
    """
    Saves the modification times to the save file.
    :param mod_time_dict: modification times
    """
    with static_data.SAVE_FILE.open('w', encoding='utf-8') as writer:
        writer.write(static_data.VERSION + '\n')
        for file, mod_time in mod_time_dict.items():
            writer.write(file + '\n' + str(mod_time) + '\n')
