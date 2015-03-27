#!/usr/bin/env python

from configparser import ConfigParser
from os import fork, execv, wait



parser = ConfigParser()
parser.read("settings.conf")
configuration = parser["CONFIGURATION"]
path = configuration["path"]
width = configuration["width"]
height = configuration["height"]
quality = configuration["quality"]
vertical_flip = configuration["vertical_flip"]
horizontal_flip = configuration["horizontal_flip"]

if fork() == 0:
    parameters = ["/opt/vc/bin/raspistill"]
    parameters.append("-w")
    parameters.append(width)
    parameters.append("-h")
    parameters.append(height)
    parameters.append("-q")
    parameters.append(quality)
    if vertical_flip == "yes":
        parameters.append("-vf")
    if horizontal_flip == "yes":
        parameters.append("-hf")
    parameters.append("-o")
    parameters.append(path + "/now.jpg")
    
    execv("/opt/vc/bin/raspistill", parameters)
else:
    wait()
    
    print("Content-type: text/html\n" \
          "Location: /html/current_view.html\n")
