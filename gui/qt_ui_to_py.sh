#!/usr/bin/env bash

for file in *.ui; do
	name=${file::-2}
	pyuic5 ${file} -o "../mp3monitoring/gui/windows/ui/"${name}"py"
done
