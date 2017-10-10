#!/bin/sh

inkscape ./data/icon_export.svg --export-png=./data/icon.png -w512 -h512

python setup.py bdist_wheel

cd ./installer
./create_installer.sh
cd ..
