cur_folder="./packages/mp3monitoring/data/"
rm -rf ${cur_folder}
mkdir -p ${cur_folder}
cp -r ../mp3monitoring/ ${cur_folder}mp3monitoring/
cp ../LICENSE.md ${cur_folder}/LICENSE.md
cp ../README.md ${cur_folder}/README.md
rm -rf ${cur_folder}/mp3monitoring/gui/

cur_folder="./packages/mp3monitoring.gui/data/"
rm -rf ${cur_folder}
mkdir -p ${cur_folder}/mp3monitoring/
cp -r ../mp3monitoring/gui/ ${cur_folder}/mp3monitoring/gui/

cur_folder="./packages/mp3monitoring.updater/data/"
rm -rf ${cur_folder}
mkdir -p ${cur_folder}

cur_folder="./packages/mp3monitoring/meta/"
cp ../LICENSE.md ${cur_folder}/LICENSE.md

mkdir -p bin
binarycreator -c ./config/config.xml -p ./packages/ --offline-only "./bin/MP3 Monitoring Setup.exe"
if [ $? -ne 0 ]; then
    exit 1
fi

exit 0
