#!/usr/bin/env python

from configparser import ConfigParser
from os.path import exists



parser = ConfigParser()
parser.read("settings.conf")
configuration = parser["CONFIGURATION"]
path = configuration["path"]

if exists(path + "/scripts/converter.pid"):
    print("Content-type: text/html\n")
    
    with open(path + "/html/waiting_for_video.html", "r", encoding="utf8") as file:
        for line in file.readlines():
            print(line, end="")
else:
    print("Content-type: text/html\n" \
          "Location: /video.mp4\n")
