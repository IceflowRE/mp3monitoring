#!/usr/bin/env bash
# executed from project root

cd ./gui
for file in *.ui; do
	name=${file::-2}
	pyuic5 ${file} -o "../mp3monitoring/gui/windows/ui/"${name}"py"
done
cd ..
