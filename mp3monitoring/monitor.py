import shutil
import time
import traceback
from pathlib import Path
from threading import Thread

from tqdm import tqdm

from tools import get_all_files_after_time, is_mp3


class Monitor:
    def __init__(self, source_dir: Path, target_dir: Path, start, pause=10, last_mod_time=0):
        """
        :param source_dir: source directory
        :param target_dir: target directory
        :param pause: pause in seconds between the scans
        :param last_mod_time: last modification time
        """
        super().__init__()
        self.startup = start
        self.status = 'Initialization'
        self.source_dir = source_dir
        self.target_dir = target_dir
        self.last_mod_time = last_mod_time
        self.__sleep_time = 1
        self.pause = pause
        self.change_pause(pause)

        self.stopping = not start
        self.pbar = ""
        self.thread = Thread(target=self.run)

        self.status = 'Stopped'
        self.check_directories()

    @classmethod
    def from_json_dict(cls, json_dict):
        source_dir = Path(json_dict['source_dir'])
        target_dir = Path(json_dict['target_dir'])
        startup = json_dict['startup']
        pause = json_dict['pause']
        last_mod_time = json_dict['last_mod_time']
        return cls(source_dir, target_dir, startup, pause, last_mod_time)

    def __str__(self):
        return "{active} | {source} | {target} | {pause}s | {status} | {startup} | {time}".format(
            active=self.thread.isAlive(),
            source=str(self.source_dir),
            target=str(self.target_dir),
            pause=str(self.pause),
            status=self.status,
            startup=self.startup,
            time=self.last_mod_time)

    def start(self):
        """

        :return:
        """
        self.status = 'Starting'
        if not self.check_directories():
            self.stopping = True
            return False
        self.stopping = False
        self.thread = Thread(target=self.run)
        self.thread.start()
        return True

    def stop(self):
        self.status = 'Stopping'
        self.stopping = True

    def run(self):
        """
        Scans a source directory every pause_s seconds, for new mp3 and copies them to the target directory.
        Warning: excepts KeyboardInterrupt!
        :return: last_mod_time
        """
        try:
            while not self.stopping:
                self.status = 'Checking for modifications'
                new_mod_time = time.time()
                new_mod_files = get_all_files_after_time(self.source_dir, after_time=self.last_mod_time)
                if new_mod_files:
                    self.status = 'Checking for mp3'
                    mp3_files = self.get_all_mp3(new_mod_files)
                    # del mp3_files
                    if mp3_files:
                        self.status = 'Copying new mp3'
                        self.copy_files_as_mp3(mp3_files)
                self.last_mod_time = new_mod_time
                self.status = 'Sleeping'
                cur_sleep = 0
                while cur_sleep < self.pause:
                    time.sleep(self.__sleep_time)
                    if self.stopping:  # dont sleep more, go to while loop check
                        break
                    cur_sleep += self.__sleep_time
        except KeyboardInterrupt:
            pass
        self.status = 'Stopped'

    def check_directories(self):
        """
        Check source and initialize target directory.
        """
        if not self.source_dir.exists():
            self.status = 'Source ({source_dir}) does not exist.'.format(source_dir=str(self.source_dir))
            return False
        elif not self.source_dir.is_dir():
            self.status = 'Source ({source_dir}) is not a directory.'.format(source_dir=str(self.source_dir))
            return False

        if not self.target_dir.exists():
            try:
                Path.mkdir(self.target_dir, parents=True)
            except PermissionError:
                self.status = 'Cant create target directory ({target_dir}). Do you have write permissions?'.format(
                    target_dir=str(self.target_dir))
            return False
        elif not self.target_dir.is_dir():
            self.status = 'Target ({target_dir}) is not a directory.'.format(target_dir=str(self.target_dir))
            return False
        return True

    def change_pause(self, pause):
        if pause < 0:
            pause = 0
        self.pause = pause
        if pause > 10 and pause % 10 == 0:
            self.__sleep_time = 10
        else:
            self.__sleep_time = 1

    def get_all_mp3(self, files):
        """
        Checks the files list for mp3.
        :param files: file list
        :return: set(file)
        """
        self.pbar = tqdm(files, desc="Checking for mp3", unit="file", leave=True, mininterval=0.2, ncols=100)
        mp3_files = {file for file in self.pbar if is_mp3(str(file))}
        self.pbar.close()
        return mp3_files

    def copy_files_as_mp3(self, files):
        """
        Copy given file list to target directory.
        :param files: set(file)
        :param target_dir: target directory
        :return: without errors copied files dict[checksum, file]
        """
        self.pbar = tqdm(files, desc="Copying new mp3", unit="mp3", leave=True, mininterval=0.2, ncols=100)
        for file in self.pbar:
            try:
                new_file = self.target_dir.joinpath(file.name)
                new_file = new_file.with_suffix('.mp3')

                while new_file.exists():
                    new_file = new_file.with_name(new_file.stem + '_d.mp3')

                shutil.copy2(str(file), str(self.target_dir))
                self.target_dir.joinpath(file.name).rename(new_file)
            except Exception:
                self.pbar.write('Couldnt copy ' + str(file))
                traceback.print_exc()
        self.pbar.refresh()
        self.pbar.close()

    def to_json_dict(self):
        return {'source_dir': str(self.source_dir.resolve()),
                'target_dir': str(self.target_dir.resolve()),
                'pause': self.pause,
                'startup': self.startup,
                'last_mod_time': self.last_mod_time
                }
