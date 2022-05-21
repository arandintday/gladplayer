#!/bin/env python
import datetime
import re
import sys
import time
import os

#Read lyrics from file
def read_file(filename):
    f = open(filename, 'r+')
    return f.read()

#Saparate every lines into list elements
def split_by_lines(filecontent):
    return filecontent.split("\n")

#Parse the timestamp from lrc file
def parse_timestamp(filecontent):
    pattern = re.compile(r'\[([0-9]*):([0-9]*)\.([0-9]*)\]')
    time_delay = []
    for l in filecontent:
        try:
            matchResult = pattern.match(l)
            secs = float("{}.{}".format(matchResult.group(2), matchResult.group(3)))
            mins = float(matchResult.group(1))
            total_secs = datetime.timedelta(minutes=mins,seconds=secs).total_seconds()
            time_delay.append(total_secs)
        except Exception as e:
            continue
    return time_delay

#Convert timestamp to delay time
def calculate_diff(time_stamp):
    diff = []
    for i in range(1,len(time_stamp)):
        diff.append(round(time_stamp[i] - time_stamp[i-1], 3))
    diff.append(round(diff[-1],3))
    return diff

#Remove the timestamp and get raw lyrics
def getLyrics(filecontent):
    lyrics = []
    for l in filecontent:
        try:
            lyrics.append(l[l.index("]")+1:])
        except:
            continue
    return lyrics

#Print method 1: Typewriter animation
def print_line_tw(content, duration):
    if len(content) > 0:
        for i in range(1, len(content)+1):
            print("{}_".format(content[:i]),end="\r")
            time.sleep(round(duration/(len(content)), 3))
    else:
        time.sleep(duration)
    print("{} ".format(content))
    return 0

#Print method 2: Directly print witout animations
def print_line_dr(content, duration):
    if len(content) > 0:
        print(content)
        time.sleep(duration)
    else:
        time.sleep(duration)
    return 0

#Print method 3: HIghlight animations
def print_line_col(content, duration):
    if len(content) > 0:
        for i in range(0,len(content)):
            print("\033[0;32m{}\033[0m{}".format(content[:i], content[i:]), end="\r")
            time.sleep(round(duration/(len(content)), 3))
    else:
        time.sleep(duration)
    print("\033[0;32m{}\033[0m".format(content))
    return 0

#Receive lyrics and delay time to display them in queue
def display_lyrics(lyrics, delay, method="1"):
    if "1" == method:
        for i in range(0, len(delay)):
            print_line_tw(lyrics[i], delay[i])
    elif "2" == method:
        for i in range(0, len(delay)):
            print_line_dr(lyrics[i], delay[i])
    elif "3" == method:
        for i in range(0, len(delay)):
            print_line_col(lyrics[i], delay[i])
    else:
        for i in range(0, len(delay)):
            print_line_tw(lyrics[i], delay[i])
    return 0

#Good old main function
def main():
    #Judge if have any parameters
    if len(sys.argv) > 1:
        lyrics = split_by_lines(read_file("{}.lrc".format(sys.argv[1])))
        try:
            display_lyrics(getLyrics(lyrics), calculate_diff(parse_timestamp(lyrics)),sys.argv[2])
        except:
            display_lyrics(getLyrics(lyrics), calculate_diff(parse_timestamp(lyrics)),"1")
        os.system("./kill.sh")
    else:
        #No parameters, show usage info
        print("GLaDLyrics v0.1\nA cli based lyric display applet written in python.\n\nUsage: \n    {} <lyrics_file_name>\nExample: \n    {} example".format(sys.argv[0], sys.argv[0]))
    return 0

#Something I don't know why but everyone add it in their code
if __name__=='__main__':
    main()

