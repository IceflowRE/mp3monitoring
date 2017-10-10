#!/bin/sh

cd ./gui/
./qt_ui_to_py.sh
cd ..

python setup.py clean --all
python setup.py bdist_wheel

cd ./installer/
./create_installer.sh
cd ..
