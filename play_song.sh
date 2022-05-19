#!/bin/sh
#Judge if it's Termux
judge_terminal(){
	getprop > /dev/null 2>&1
	if [ $? -eq 0 ];then
    		#clear
    		#nohup play-audio $1.mp3 > /dev/null 2>&1 &
    		#./lyrics_display.py $1
		termux_method $1
	else
    		#clear
		#nohup mplayer $1.mp3 > /dev/null 2>&1 &
    		#./lyrics_display.py $1
		linux_method $1
	fi
}
termux_method(){
	clear
	nohup play-audio $1.mp3 > /dev/null 2>&1 &
	./lyrics_display.py $1
}
linux_method(){
	clear
	nohup mplayer $1.mp3 > /dev/null 2>&1 &
	./lyrics_display.py $1
}
judge_terminal $1
