#!/bin/sh
# executed from project root

py_version="$1"

./scripts/qt_ui_to_py.sh

python setup.py clean --all
python setup.py bdist_wheel --python-tag "$py_version"

app_version=$(grep -oP "VERSION\s=\s'\K\w+.\w+.\w+" ./mp3monitoring/data/static.py)
./scripts/create_installer.sh "$py_version" "$app_version"
