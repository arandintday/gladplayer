# Attention

This project is still under early development and really buggy. Think twice if you want to use it.

## GLaDPlayer

A small music visualizing tool in terminal.

## ~~Bugs~~Features

* Print lyrics in your terminal (Mostly synchronous with music)
* Print ASCII art in your terminal (ascii file is needed)
* Can run in Android (With Termux)

## Requirements

* tmux
* mplayer
* python3
* audio-play (If you are using Termux)

## Basic Usage (without ascii art)

Clone this repository and put some `*.mp3` and `*.lrc` files in it's main directory. (Their name should be the same) Then open your terminal, enter this directory and run
```shell
./main.sh <your song file name>
```
Example:

If your song's file name is `sus.mp3` and the lyric file name is `sus.lrc`, then your command will be
```shell
./main.sh sus
```

## Play with ascii art

You should first copy-pasta your favorite ascii into a new *.txt file and put them into the `ascii` folder. (or not, if you think the default ones are ok)

Then create a `*.ascii` file in this repository's main directory, it should be looking like this:

```
[00:00.00]
[minutes:seconds.decimal_seconds]<Your ascii file's name>
...
```
The things in square brackets are timestamps, it'll decide when it display your specified ascii art in your terminal.
Example:
```
[00:00.00]
[00:01.20]aperture
[00:02.40]fire
[00:08.20]nuclear
...
```
If every thing went right, you can now play it with ascii art you just specified.