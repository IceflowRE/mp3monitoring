import subprocess
import sys
from argparse import ArgumentParser
from pathlib import Path


def gen_logo_ico():
    sizes = ["16", "32", "64", "128", "256", "512", "1024"]
    Path("./build").mkdir(exist_ok=True)
    for size in sizes:
        subprocess.run(["inkscape", "-w", str(size), "-h", str(size), "-o", f"./build/{size}.png", "./mp3monitoring/gui/pkg_data/logo.svg"])
    subprocess.run(["magick", "convert", *[f"./build/{size}.png" for size in sizes], "./mp3monitoring/gui/pkg_data//logo.ico"], stdout=sys.stdout,
                   stderr=sys.stderr)


def ui_to_py(pyside2_uic: str = "pyside2-uic"):
    output_dir = Path("./mp3monitoring/gui/ui")
    for ui_file in Path("./gui").glob("*.ui"):
        subprocess.run([pyside2_uic, str(ui_file), "-o", output_dir.joinpath(ui_file.stem + '.py')], stdout=sys.stdout, stderr=sys.stderr)


if __name__ == '__main__':
    parser = ArgumentParser(prog="MP3 Monitoring Development Tools")

    subparsers = parser.add_subparsers(dest="tool", help='')

    parser_uic = subparsers.add_parser('uic', help='invoke pyside2-uic and create python files')
    parser_uic.add_argument('--exec', dest='uic_executable', default="pyside2-uic", type=str, metavar='uic executable',
                            help='pyside-uic executable path/name')
    parser_ico = subparsers.add_parser('ico', help='generate an ico from the logo svg')

    if sys.version_info[0] < 3 or sys.version_info[1] < 8:
        sys.exit('Only Python 3.8 or greater is supported. You are using:' + sys.version)

    args = parser.parse_args(sys.argv[1:])
    if args.tool == "uic":
        ui_to_py(args.uic_executable)
    elif args.tool == "ico":
        gen_logo_ico()
