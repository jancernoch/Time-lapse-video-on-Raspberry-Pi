#!/usr/bin/env python

from cgi import FieldStorage
from configparser import ConfigParser
from os import fork, execv, remove, symlink



parser = ConfigParser()
parser.read("settings.conf")
configuration = parser["CONFIGURATION"]
path = configuration["path"]

form = FieldStorage()

files = form.getlist("files")

if form["process"].value == "download":
    i = 0
    for file in files:
        symlink(path + "/data/" + file, path + "/data/image_{0:08d}.jpg".format(i))
        i = i + 1
    
    if fork() == 0:
        execv(path + "/scripts/converter.sh", [path + "/scripts/converter.sh"])
    else:
        print("Content-type: text/html\n" \
              "Location: /cgi/waiting_for_video.py\n")
        
elif form["process"].value == "delete":
    for file in files:
        remove(path + "/data/" + file)

    print("Content-type: text/html\n" \
          "Location: /cgi/download_video.py\n")
