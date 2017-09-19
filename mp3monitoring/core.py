import json
import sys
import traceback
from argparse import ArgumentParser
from pathlib import Path

import tools
from data import dynamic, static
from monitor import Monitor

job_dict = {}


def _init():
    """
    Initialization save directory.
    """
    home = dynamic.SAVE_FILE.parent
    try:
        if not home.exists():
            home.mkdir(parents=True)
        if not dynamic.SAVE_FILE.exists():
            json_dict = {'information': {'version': static.VERSION}}
            with dynamic.SAVE_FILE.open('w', encoding='utf-8') as writer:
                json.dump(json_dict, writer, indent=4)
    except PermissionError:
        print('Cant write to config folder ({home}). Make sure you have write permissions.'.format(home=str(home)))

    # load save file
    try:
        print('Load save file.')
        save_dict = tools.load_config_data(dynamic.SAVE_FILE)
    except Exception:
        print('Could not load save file.')  # TODO: ask user
        traceback.print_exc()
        sys.exit(1)
    # TODO: version not used
    if 'jobs' in save_dict:
        for job in save_dict['jobs']:
            add_new_monitor(Monitor.from_json_dict(job))


def start():
    """
    Entry point into program.
    """
    global job_dict
    if sys.version_info[0] < 3 or sys.version_info[1] < 6:
        sys.exit('Only Python 3.6 or greater is supported. You are using: {version}'.format(version=sys.version))

    parser = ArgumentParser(prog='mp3-monitoring',
                            description='Monitors a folder and copies mp3s to another folder. Quit with Ctrl+C.')
    parser.add_argument('-v', '--version', action='version', version=static.VERSION)
    parser.add_argument('-j', '--job', dest='job_list', nargs=3, action='append', metavar=('source', 'target', 'pause'),
                        help='Monitors the source and copies to target directory and adds a pause in seconds between every check.')
    parser.add_argument('--ignore_save', dest='no_save', default=False, action='store_true',
                        help='ignore the last modification time from save file (default: %(default)s)')
    parser.add_argument('--gui', dest='gui', default=False, action='store_true',
                        help='open the gui (default: %(default)s)')

    # init
    args = parser.parse_args()
    _init()

    # configure threads
    add_new_jobs(job_dict, args.job_list, args.no_save)  # job_dict will be modified

    if args.gui:
        gui()

    shutdown()


def add_new_monitor(monitor):
    global job_dict
    job_dict[str(monitor.source_dir)] = monitor
    if monitor.startup:
        if not monitor.start():
            monitor.startup = False
            print(monitor, monitor.status)


def add_new_jobs(jobs_dict, job_list, no_save):
    """
    Will overwrite existing monitoring jobs.
    :param jobs_dict: will be modified
    :param job_list:
    :param no_save:
    :return:
    """
    if job_list is None:
        return
    for task in job_list:
        source_dir = Path(task[0])
        target_dir = Path(task[1])
        pause = int(task[2])

        if str(source_dir) in jobs_dict and not no_save:  # check if the source already exists
            last_mod_time = jobs_dict[str(source_dir)].last_mod_time
        else:
            last_mod_time = 0

        add_new_monitor(Monitor(source_dir, target_dir, True, last_mod_time=last_mod_time, pause=pause))


def gui():
    try:
        from PyQt5.QtWidgets import QApplication
    except ImportError:
        print('PyQt5 not installed, you can not use the gui.')
        return
    try:
        from gui.windows.main import MainWindow
    except ImportError:
        print('blubs')
        return
    app = QApplication([])
    main_window = MainWindow(app)
    main_window.show()
    sys.exit(app.exec_())


def shutdown(signal=None):
    """

    :param signal: signal of the gui callback
    :return:
    """
    global job_dict
    if signal is not None:
        signal.emit("Stopping monitoring threads")
    for job in job_dict.values():
        job.stop()
    # wait for ending
    for monitor in job_dict.values():
        if monitor.thread.isAlive():
            monitor.thread.join()

    if signal is not None:
        signal.emit("Save save file")
    tools.save_config_data(job_dict, dynamic.SAVE_FILE)
