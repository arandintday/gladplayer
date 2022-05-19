#!/bin/env python
from datetime import datetime
import re
import sys
import time
import datetime
import os

def read_file(filename):
    f = open(filename, 'r+')
    return f.read()

def split_by_lines(filecontent):
    return filecontent.split("\n")

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

def calculate_diff(time_stamp):
    diff = []
    for i in range(1,len(time_stamp)):
        diff.append(round(time_stamp[i] - time_stamp[i-1], 3))
        #diff.append(time_stamp[i] - time_stamp[i-1])
    diff.append(0.0)
    return diff

def get_ascii_name(filecontent):
    ascii_name = []
    for l in filecontent:
        try:
            ascii_name.append(l[l.index("]")+1:])
        except:
            continue
    return ascii_name

def print_ascii_art(content, duration):
    if len(content) > 0:
        try:
            os.system("clear && cat './ascii/{}.txt'".format(content))
        except:
            print("ASCII art file load failed!")
        time.sleep(duration)
    else:
        time.sleep(duration)
    return 0

def display_ascii(ascii_list, delay):
    for i in range(0, len(delay)):
        #print(delay[i])
        print_ascii_art(ascii_list[i], delay[i])
    return 0

def main():
    if len(sys.argv) > 1:
        ascii_name = split_by_lines(read_file("{}.ascii".format(sys.argv[1])))
        display_ascii(get_ascii_name(ascii_name), calculate_diff(parse_timestamp(ascii_name)))
    else:
        print("GLaDASCII v0.1\nA cli based ascii art display applet written in python.\n\nUsage: \n    {} <ascii_file_name>\nExample: \n    {} example".format(sys.argv[0], sys.argv[0]))
    return 0

if __name__=='__main__':
    main()

