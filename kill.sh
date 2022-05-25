#!/bin/bash
#pkill python > /dev/null 2>&1
pkill play-audio > /dev/null 2>&1
pkill mplayer > /dev/null 2>&1
tmux kill-server > /dev/null 2>&1
#pkill tmux > /dev/null 2>&1
