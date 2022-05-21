#!/bin/bash

#Judge if it's Termux
judge_terminal(){
	getprop > /dev/null 2>&1
	if [ $? -eq 0 ];then
    		#clear
    		#nohup play-audio $1.mp3 > /dev/null 2>&1 &
    		#./lyrics_display.py $1
		termux_method $1 $2
	else
    		#clear
		#nohup mplayer $1.mp3 > /dev/null 2>&1 &
    		#./lyrics_display.py $1
		linux_method $1 $2
	fi
}

#judge if files are exist
if_exist(){
	find ./$1.mp3 > /dev/null 2>&1
	if [ $? -eq 0 ];then
		find ./$1.lrc > /dev/null 2>&1
		if [ $? -eq 0 ];then
			judge_terminal $1 $2
		else
			echo '[-] lyric file not found!'
			sleep 3
		fi
	else
		echo '[-] music file not found!'
		sleep 3
	fi
}

#When it runs in termux
termux_method(){
	clear
	nohup play-audio $1.mp3 > /dev/null 2>&1 &
	./lyrics_display.py $1 $2
}

#When it runs in linux
linux_method(){
	clear
	nohup mplayer $1.mp3 > /dev/null 2>&1 &
	./lyrics_display.py $1 $2
}

if_exist $1 $2
