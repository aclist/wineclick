#!/bin/bash
#hold and drag left button

file=/app_path/wineclick
[[ ! -f $file ]] && touch $file
xdotool mousemove 500 200
echo left_down >> $file
xdotool mousemove 200 100
echo left_up >> $file
