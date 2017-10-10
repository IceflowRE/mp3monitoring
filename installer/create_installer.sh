#!/bin/sh

cur_folder="./hybrid/config/data"
rm -rf ${cur_folder}
mkdir -p ${cur_folder}
inkscape ../mp3monitoring/pkg_data/gui/icon_export.svg --export-png=${cur_folder}/icon.png -w512 -h512

cur_folder="./hybrid/packages/mp3monitoring/data/"
rm -rf ${cur_folder}
mkdir -p ${cur_folder}
cp ../README.md ${cur_folder}/README.md
cp ../dist/MP3_Monitoring-1.0.0-py3-none-any.whl ${cur_folder}/MP3_Monitoring-1.0.0-py3-none-any.whl

cur_folder="./hybrid/packages/mp3monitoring/meta/"
cp ../LICENSE.md ${cur_folder}/LICENSE.md

mkdir -p bin
binarycreator -c ./hybrid/config/config.xml -p ./hybrid/packages/ --offline-only "./bin/MP3 Monitoring Hybrid Setup.exe"
if [ $? -ne 0 ]; then
    exit 1
fi

exit 0
