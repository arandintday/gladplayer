#!/bin/bash
split_screen(){
	session_name="sec"
	#commands_1="cmatrix"
	#commands_2="cmatrix"
	tmux new-session -d -s $session_name $1
	tmux split-window -d -t $session_name:0 -p45 -h $3
	tmux selectp -t 1
	tmux split-window -d -t $session_name:0 -p55 -v $2
	#tmux select-layout -t $session_name:0 even-horizontal
	tmux attach-session -t $session_name
}
split_screen "./play_song.sh $1 $2" "./ascii_display.py $1" $3
