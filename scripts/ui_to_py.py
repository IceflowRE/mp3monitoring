from os import system
from pathlib import Path

if __name__ == '__main__':
    output_dir = Path("./mp3monitoring/gui/ui")
    for ui_file in Path("./gui").glob("*.ui"):
        print(f"pyuic5 {str(ui_file)} -o {output_dir.joinpath(ui_file.stem + '.py')}")
        system(f"pyuic5 {str(ui_file)} -o {output_dir.joinpath(ui_file.stem + '.py')}")
