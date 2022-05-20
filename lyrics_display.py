#!/bin/env python
from datetime import datetime
import re
import sys
import time

#Read file content from file
def read_file(filename):
    f = open(filename, 'r+')
    return f.read()

#Split lyrics into list
def split_by_lines(filecontent):
    return filecontent.split("\n")

#Parsing the timestamp from lrc file
def parse_timestamp(filecontent):
    pattern = re.compile(r'\[([0-9]*):([0-9]*)\.([0-9]*)\]')
    time_delay = []
    #In developing
    for l in filecontent:
        try:
            matchResult = pattern.match(l)
            #matchResult = pattern.match("[33:4.214]anfaifncoanca")
            #print(matchResult.groups())
            secs = float("{}.{}".format(matchResult.group(2), matchResult.group(3)))
            mins = float(matchResult.group(1))
            total_secs = datetime.timedelta(minutes=mins,seconds=secs).total_seconds()
            #print(total_secs)
            time_delay.append(total_secs)
        except Exception as e:
            #print("[-] E:{}".format(e))
            continue
    return time_delay

#Convert timestamps into delay time
def calculate_diff(time_stamp):
    diff = []
    for i in range(1,len(time_stamp)):
        diff.append(round(time_stamp[i] - time_stamp[i-1], 3))
        #diff.append(time_stamp[i] - time_stamp[i-1])
    diff.append(round(diff[-1],3))
    return diff

#Remove the timestamps and get the raw lyrics
def getLyrics(filecontent):
    lyrics = []
    for l in filecontent:
        try:
            lyrics.append(l[l.index("]")+1:])
        except:
            continue
    return lyrics

#Display Method 1: Typewriter effect
def print_line_tw(content, duration):
    if len(content) > 0:
        for i in range(1, len(content)+1):
            print("{}_".format(content[:i]),end="\r")
            time.sleep(round(duration/(len(content)), 3))
    else:
        time.sleep(duration)
    print("{} ".format(content))
    return 0

#Display Method 2: Directly show'em
def print_line_dr(content, duration):
    if len(content) > 0:
        print(content)
        time.sleep(duration)
    else:
        time.sleep(duration)
    return 0

#Display Method 3: Highlight effect
def print_line_col(content, duration):
    if len(content) > 0:
        for i in range(0,len(content)):
            print("\033[0;32m{}\033[0m{}".format(content[:i], content[i:]), end="\r")
            time.sleep(round(duration/(len(content)), 3))
    else:
        time.sleep(duration)
    print("\033[0;32m{}\033[0m".format(content))
    return 0

#Receive lyrics and delay times to display the lyrics
def display_lyrics(lyrics, delay):
    for i in range(0, len(delay)):
        print_line_tw(lyrics[i], delay[i])
    return 0

#Good old main function
def main():
    if len(sys.argv) > 1:
        #Get the parameters from input
        lyrics = split_by_lines(read_file("{}.lrc".format(sys.argv[1])))
        display_lyrics(getLyrics(lyrics), calculate_diff(parse_timestamp(lyrics)))
    else:
        #If nothing received, show usage instructions
        print("GLaDLyrics v0.1\nA cli based lyric display applet written in python.\n\nUsage: \n    {} <lyrics_file_name>\nExample: \n    {} example".format(sys.argv[0], sys.argv[0]))
    return 0

#Something important but I don't know why what and how
if __name__=='__main__':
    main()

