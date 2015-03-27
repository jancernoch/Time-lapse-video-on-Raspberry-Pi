#!/usr/bin/env python

from configparser import ConfigParser
from os import listdir



parser = ConfigParser()
parser.read("settings.conf")
configuration = parser["CONFIGURATION"]
path = configuration["path"]

print("Content-type: text/html\n")

with open(path + "/html/download_video.html", "r", encoding="utf8") as file:
    for line in file.readlines():
        if "files_tag" in line:
            pictures = listdir(path + "/data")
            pictures.sort()
        
            for picture in pictures:
                print("<option value=" + picture + ">" + picture + "</option>")
        else:
            print(line, end="")
