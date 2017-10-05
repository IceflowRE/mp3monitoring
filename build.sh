#!/bin/sh

python setup.py bdist_wheel

cd ./installer
./create_installer.sh
cd ..
