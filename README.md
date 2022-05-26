# Attention

This project is still under early development and really buggy. Think twice if you want to use it.

## Demonstration

https://www.reddit.com/r/Portal/comments/ut63gx/i_made_a_small_tool_to_play_still_alive_in_actual/

## GLaDPlayer

"Genetic Lifeform and Disk Player" - A small terminal based music visualizing gadget written in python.
The name is inspired by Valve's famous video game "Portal".

## To do list

* Automatically change tmux split direction by detecting terminal scale
* ~~Add a new panel to display another effects~~Done
* Automatically clear the lyrics if it reached the maxium lines in terminal
* Add some decorations to tmux panels
* ~~Add an option to change the lyrics displaying method~~Done
* Add a custom exit hot key
* ~~Add error handler~~Done
* Add more file type support
* Add custom command support in ascii file(maybe)
* Add a installation script (maybe)
* ~~Bake a cake~~

## ~~Bugs~~Features

* Print lyrics in your terminal (Mostly synchronous with music)
* Print ASCII art in your terminal (ascii file is needed)
* Can display any custom command in an additional panel
* Can run in Android (With Termux)

## Requirements

* tmux
* mplayer
* python3
* audio-play (If you are using Termux)

## Basic Usage (without ascii art)

Clone this repository and put some `*.mp3` and `*.lrc` files in it's main directory. (Their name should be the same) Then open your terminal, enter this directory and run
```shell
./main.sh <your song file name> <display_effect(optional)> <Your custom command(optional)>
```

Lyrics display effects:
1
* The type writer effect(Default)
2
* No effect
3
* Highlight effect

Example:
If your song's file name is `sus.mp3` and the lyric file name is `sus.lrc` and you want using the highlight effect and let the third panel run htop, then your command will be:
```shell
./main.sh sus 3 htop
```

## Play with ascii art

You should first copy-pasta your favorite ascii into a new `*.txt` file and put them into the `ascii` folder. (or not, if you think the default ones are ok)

Then create a `<song file's name>.ascii` file in this repository's main directory, it should be looking like this:

```
[00:00.00]
[minutes:seconds]<Your ascii file's name>
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
