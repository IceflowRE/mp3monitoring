import shutil
import time
import traceback
from pathlib import Path
from threading import Thread

from tqdm import tqdm

from tools import get_all_files_after_time, is_mp3


class Monitor:
    def __init__(self, source_dir: Path, target_dir: Path, start, pause_s=10, last_mod_time=0):
        """
        :param source_dir: source directory
        :param target_dir: target directory
        :param pause_s: scan every X seconds
        :param last_mod_time: last modification time
        """
        super().__init__()
        self.stopping = not start
        self.status = 'Initialization'
        self.source_dir = source_dir
        self.target_dir = target_dir
        self.pause_s = pause_s
        if pause_s % 10 == 0:
            self.sleep_time = 10
        else:
            self.sleep_time = 1
        self.last_mod_time = last_mod_time
        self.pbar = ""
        self.thread = Thread(target=self.run)

    def __str__(self):
        return "{active} | {source} | {target} | {pause_s}s | {status}".format(active=self.thread.isAlive(),
                                                                               source=str(self.source_dir),
                                                                               target=str(self.target_dir),
                                                                               pause_s=str(self.pause_s),
                                                                               status=self.status)

    def start(self):
        self.status = 'Starting'
        self.stopping = False
        self.thread = Thread(target=self.run)
        self.thread.start()

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
                for i in range(self.pause_s):
                    time.sleep(self.sleep_time)
                    if self.stopping:  # dont sleep more, go to while loop check
                        break
        except KeyboardInterrupt:
            pass
        self.status = 'Stopped'

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
