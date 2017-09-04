import shutil
import time
import traceback
from pathlib import Path

import mutagen.mp3
from tqdm import tqdm

from mp3monitoring import static_data


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


def get_all_files_after_mtime(directory, after_time=0):
    """
    Check all files in the given directory if access time after the given time.
    :param directory: directory which will be checked
    :param after_time: time in seconds (unixtime)
    :return: list of modified files after time
    """
    directory = directory.glob('**/*')
    return [file for file in directory if (file.is_file() and (file.stat().st_mtime > after_time))]


def get_all_mp3(files):
    """
    Checks the files list for mp3.
    :param files: file list
    :return: set(file)
    """
    pbar = tqdm(files, desc="Check for mp3", unit="file", leave=True, mininterval=0.2, ncols=100)
    mp3_files = {file for file in pbar if is_mp3(str(file))}
    pbar.close()
    return mp3_files


def copy_files_as_mp3(files, target_dir: Path):
    """
    Copy given file list to target directory.
    :param files: set(file)
    :param target_dir: target directory
    :return: without errors copied files dict[checksum, file]
    """
    pbar = tqdm(files, desc="Copy new mp3", unit="mp3", leave=True, mininterval=0.2, ncols=100)
    for file in pbar:
        try:
            new_file = target_dir.joinpath(file.name)
            new_file = new_file.with_suffix('.mp3')

            while new_file.exists():
                new_file = new_file.with_name(new_file.stem + '_d.mp3')

            shutil.copy2(str(file), str(target_dir))
            target_dir.joinpath(file.name).rename(new_file)
        except Exception:
            pbar.write('Couldnt copy ' + str(file))
            traceback.print_exc()
    pbar.refresh()
    pbar.close()


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
                save_dict[line] = int(float(next(it)))
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


def monitoring(source_dir, target_dir, pause_s=10, last_mod_time=0):
    """
    Scans a source directory every pause_s seconds, for new mp3 and copies them to the target directory.
    Warning: excepts KeyboardInterrupt!
    :param source_dir: source directory
    :param target_dir: target directory
    :param pause_s: scan every X seconds
    :param last_mod_time: last modification time
    :return: last_mod_time
    """
    try:
        while True:
            print('=' * 50)
            print('Check for modifications.')
            new_mod_time = time.time()
            new_mod_files = get_all_files_after_mtime(source_dir, after_time=last_mod_time)
            if new_mod_files:
                mp3_files = get_all_mp3(new_mod_files)
                # del mp3_files
                if mp3_files:
                    copy_files_as_mp3(mp3_files, target_dir)
            last_mod_time = new_mod_time
            time.sleep(pause_s)
    except KeyboardInterrupt:
        pass
    return last_mod_time
