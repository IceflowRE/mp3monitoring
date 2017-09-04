import sys
import traceback
from argparse import ArgumentParser
from pathlib import Path

from mp3monitoring import Tools
from mp3monitoring import StaticData


def _init(source_dir, target_dir):
    """
    Initialization of directories and files.
    :param source_dir: source directory
    :param target_dir: mp3 target folder
    """
    if not source_dir.exists() or not source_dir.is_dir():
        print('Source does not exist or is not a directory.')
        sys.exit(1)

    try:
        if not target_dir.exists():
            Path.mkdir(target_dir, parents=True)
        elif not target_dir.is_dir():
            print('Target directory is not a directory.')
    except PermissionError:
        print('Cant create target directory ' + str(target_dir) + '. Make sure you have write permissions.')
        sys.exit(1)
    except Exception as ex:
        print('Something went wrong: ' + traceback.format_exc(ex.__traceback__))
        sys.exit(1)

    home = StaticData.SAVE_FILE.parent
    try:
        if not home.exists():
            home.mkdir(parents=True)
        if not StaticData.SAVE_FILE.exists():
            with StaticData.SAVE_FILE.open('w', encoding='utf-8') as writer:
                writer.write(StaticData.VERSION + '\n')
    except PermissionError:
        print('Cant write to config folder ' + str(home) + '. Make sure you have write permissions.')


def start():
    """
    Entry point into program.
    """
    if sys.version_info[0] < 3 or sys.version_info[1] < 6:
        sys.exit('Only Python 3.6 or greater is supported. You are using:' + sys.version)

    parser = ArgumentParser(prog='mp3-monitoring',
                            description='Monitors a folder and copies mp3s to another folder. Quit with Ctrl+C.')
    parser.add_argument('-v', '--version', action='version', version=(StaticData.VERSION))
    parser.add_argument('-s', dest='source_dir', default='./', required=True,
                        help='source directry which will be monitored (default: %(default)s)')
    parser.add_argument('-t', dest='target_dir', default='./mp3', required=True,
                        help='target directory where mp3 will be copied (default: %(default)s)')
    parser.add_argument('--no_save', dest='no_save', default=False, action='store_true',
                        help='ignore the last modification time from save file (default: %(default)s)')
    parser.add_argument('--pause', dest='pause_s', default=10, type=int,
                        help='pause after one check in seconds (default: %(default)s)')

    args = parser.parse_args()
    source_dir = Path(args.source_dir)
    target_dir = Path(args.target_dir)

    _init(source_dir, target_dir)

    try:
        print('Load save file.')
        mod_time_dict = Tools.load_config_data()
    except Exception:
        print('Could not load save file.')  # TODO: ask user
        traceback.print_exc()
        sys.exit(1)

    if not args.no_save:
        last_mod_time = mod_time_dict.get(str(source_dir.resolve()), 0)
    else:
        last_mod_time = 0

    last_mod_time = Tools.monitoring(source_dir, target_dir, last_mod_time=last_mod_time, pause_s=args.pause_s)
    print('Quit program.')
    mod_time_dict[str(source_dir.resolve())] = last_mod_time
    print('Save save file.')
    Tools.save_config_data(mod_time_dict)
