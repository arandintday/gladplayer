#!/bin/bash
split_screen(){
	session_name="sec"
	#commands_1="cmatrix"
	#commands_2="cmatrix"
	tmux new-session -d -s $session_name $1
	tmux split-window -d -t $session_name:0 -p20 -h $2
	tmux select-layout -t $session_name:0 even-horizontal
	tmux attach-session -t $session_name
}
split_screen "./play_song.sh $1" "./ascii_display.py $1"
