#!/bin/sh
# executed from project root

py_version="$1"
app_version=$(grep -oP "VERSION\s=\s'\K([\w\W]*)'" ./mp3monitoring/data/static.py)
app_version=${app_version:: -1}

./scripts/build.sh "$py_version"
pip install --upgrade --no-cache ./dist/MP3_Monitoring-"$app_version"-"$py_version"-none-any.whl[dev]
