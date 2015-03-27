#!/usr/bin/env python

from configparser import ConfigParser
from os import fork, execv



parser = ConfigParser()
parser.read("settings.conf")
configuration = parser["CONFIGURATION"]
path = configuration["path"]

if fork() == 0:
    execv(path + "/scripts/start_photographer.sh", [path + "/scripts/start_photographer.sh"])
else:
    print("Content-type: text/html\n" \
          "Location: /cgi/settings.py\n")
