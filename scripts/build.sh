#!/bin/sh
# executed from project root

py_version="$1"

./scripts/qt_ui_to_py.sh

echo $(python --version)
python setup.py clean --all
python setup.py bdist_wheel --python-tag "$py_version"
