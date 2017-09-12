import sys
import traceback
from argparse import ArgumentParser
from pathlib import Path

import tools
from data import dynamic, static
from monitor import Monitor

job_dict = {}
time_dict = {}


def _init():
    """
    Initialization save directory.
    """
    global time_dict
    home = dynamic.SAVE_FILE.parent
    try:
        if not home.exists():
            home.mkdir(parents=True)
        if not dynamic.SAVE_FILE.exists():
            with dynamic.SAVE_FILE.open('w', encoding='utf-8') as writer:
                writer.write(static.VERSION + '\n')
    except PermissionError:
        print('Cant write to config folder ' + str(home) + '. Make sure you have write permissions.')

    # load save file
    try:
        print('Load save file.')
        time_dict = tools.load_config_data()
    except Exception:
        print('Could not load save file.')  # TODO: ask user
        traceback.print_exc()
        sys.exit(1)


def start():
    """
    Entry point into program.
    """
    global time_dict, job_dict
    if sys.version_info[0] < 3 or sys.version_info[1] < 6:
        sys.exit('Only Python 3.6 or greater is supported. You are using:' + sys.version)

    parser = ArgumentParser(prog='mp3-monitoring',
                            description='Monitors a folder and copies mp3s to another folder. Quit with Ctrl+C.')
    parser.add_argument('-v', '--version', action='version', version=static.VERSION)
    parser.add_argument('-d', '--directory', dest='dir_list', nargs=2, action='append', required=True,
                        help='source and target directory which will be monitored (default: %(default)s)')
    parser.add_argument('--no_save', dest='no_save', default=False, action='store_true',
                        help='ignore the last modification time from save file (default: %(default)s)')
    parser.add_argument('--pause', dest='pause_s', default=10, type=int,
                        help='pause between the checks in seconds (default: %(default)s)')
    parser.add_argument('--gui', dest='gui', default=False, action='store_true',
                        help='open the gui (default: %(default)s)')

    # init
    args = parser.parse_args()
    _init()

    # configure threads
    create_jobs(job_dict, time_dict, args.dir_list, args.no_save, args.pause_s)  # job_dict will be modified
    # start threads
    for thread in job_dict.values():
        thread.start()

    if args.gui:
        gui()

    for thread in job_dict.values():
        thread.join()
    shutdown()


def import_pyqt():
    try:
        import PyQt5
        from PyQt5.QtWidgets import QApplication
    except ImportError:
        pass  # module doesn't exist, deal with it.


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


def create_jobs(jobs_dict, times_dict, dir_list, no_save, pause_s):
    """

    :param jobs_dict: will be modified
    :param times_dict:
    :param dir_list:
    :param no_save:
    :param pause_s:
    :return:
    """
    for task in dir_list:
        source_dir = Path(task[0])
        target_dir = Path(task[1])

        try:
            init_monitor_dir(source_dir, target_dir)
        except FileNotFoundError:
            print('Source ({source_dir}) does not exist or is not a directory.'.format(source_dir=str(source_dir)))
            break
        except NotADirectoryError:
            print('Target directory ({target_dir}) is not a directory.'.format(target_dir=str(target_dir)))
            break
        except PermissionError:
            print('Cant create target directory ({target_dir}). Make sure you have write permissions.'.format(
                target_dir=str(target_dir)))
            break
        except Exception as ex:
            print('Something went wrong: ' + traceback.format_exc(ex.__traceback__))
            break

        if no_save:
            last_mod_time = 0
        else:
            last_mod_time = times_dict.get(str(source_dir.resolve()), 0)

        cur_monitor = Monitor(source_dir, target_dir, last_mod_time=last_mod_time, pause_s=pause_s)
        jobs_dict[str(source_dir.resolve())] = cur_monitor


def gui():
    try:
        from PyQt5.QtWidgets import QApplication
        from gui.main import MainWindow
    except ImportError:
        print('PyQt5 not installed, you can not use the gui.')
        sys.exit(1)
    app = QApplication([])
    main_window = MainWindow(app)
    main_window.show()
    sys.exit(app.exec_())


def shutdown(signal=None):
    """

    :param signal: signal of the gui callback
    :return:
    """
    global time_dict, job_dict
    if signal is not None:
        signal.emit("Stopping monitoring threads")
    for job in job_dict.values():
        job.active = False
    # wait for ending
    for thread in job_dict.values():
        thread.join()

    # update times
    if signal is not None:
        signal.emit("Update times")
    time_dict = {source_dir: thread.last_mod_time for source_dir, thread in job_dict.items()}

    if signal is not None:
        signal.emit("Save save file")
    tools.save_config_data(time_dict)
