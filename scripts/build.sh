#!/bin/sh
# executed from project root

./scripts/qt_ui_to_py.sh

python setup.py clean --all
python setup.py bdist_wheel --python-tag "$1"

./scripts/create_installer.sh
