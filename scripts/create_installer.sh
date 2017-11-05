#!/bin/sh
# executed from project root

cur_folder="./installer/hybrid/config/data"
rm -rf ${cur_folder}
mkdir -p ${cur_folder}
inkscape ./mp3monitoring/pkg_data/gui/icon_export.svg --export-png=${cur_folder}/icon.png -w512 -h512

cur_folder="./installer/hybrid/packages/mp3monitoring/data/"
rm -rf ${cur_folder}
mkdir -p ${cur_folder}
cp ./README.md ${cur_folder}/README.md
cp ./dist/MP3_Monitoring-1.0.3-py36-none-any.whl ${cur_folder}/MP3_Monitoring-1.0.3-py36-none-any.whl

cur_folder="./installer/hybrid/packages/mp3monitoring.gui/data/"
rm -rf ${cur_folder}
mkdir -p ${cur_folder}
cp ./installer/icon.ico ${cur_folder}/icon.ico

cur_folder="./installer/hybrid/packages/mp3monitoring/meta/"
cp ./LICENSE.md ${cur_folder}/LICENSE.md

mkdir -p bin
binarycreator -c ./installer/hybrid/config/config.xml -p ./installer/hybrid/packages/ --offline-only "./installer/bin/MP3 Monitoring Hybrid Setup 1_0_3.exe"
if [ $? -ne 0 ]; then
    exit 1
fi

exit 0