#!/bin/env python
import re
import sys
import time
import datetime
import os
import subprocess

CLI_PATTERN = '$'

def read_file(filename):
    try:
        f = open(filename, 'r+')
        return f.read()
    except:
        print("[-] ASCII file not found!")
        sys.exit()

def split_by_lines(filecontent):
    return filecontent.split("\n")

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

def calculate_diff(time_stamp):
    diff = []
    for i in range(1,len(time_stamp)):
        diff.append(round(time_stamp[i] - time_stamp[i-1], 3))
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
        if CLI_PATTERN in content:
            try:
                #not working
                os.system("timeout {}s {}".format(duration,content[content.index(CLI_PATTERN)+1:]))
                #still not working
                #command_list = content[content.index(CLI_PATTERN)+1:].split(" ")
                #print(command_list)
                #process = subprocess.run(commands_list, timeout=duration, text=True, capture_output=True)
            except:
                print("Command run failed!")
        else:
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

