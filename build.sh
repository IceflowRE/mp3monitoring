#!/bin/sh

cd ./gui/
./qt_ui_to_py.sh
cd ..

inkscape ./data/icon_export.svg --export-png=./data/icon.png -w512 -h512

python setup.py clean --all
python setup.py bdist_wheel

cd ./installer/
./create_installer.sh
cd ..
