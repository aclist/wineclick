#!/bin/bash
# autoclick with toggle

file=/app_path/wineclick
[[ ! -f $file ]] && touch $file
switch=sw

keep_clicking(){
	while true; do
		echo left >> $file
		sleep 0.1s
	done
}

if [[ ! -f $switch ]]; then
	touch $switch
	keep_clicking
else
	rm $switch
	echo exit >> $file
	rm $file
	pkill -f toggle.sh
fi
