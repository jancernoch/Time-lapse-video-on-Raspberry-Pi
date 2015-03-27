#!/usr/bin/env python

from cgi import FieldStorage
from configparser import ConfigParser



form = FieldStorage()

parser = ConfigParser()
parser.read("settings.conf")
configuration = parser["CONFIGURATION"]

try:
    width = int(form["width"].value)
    
    if width < 320:
        width = 320
    elif width > 1280:
        width = 1280
    
    configuration["width"] = str(width)
except ValueError:
    pass

try:
    height = int(form["height"].value)
    
    if height < 240:
        height = 240
    elif height > 720:
        height = 720
    
    configuration["height"] = str(height)
except ValueError:
    pass

try:
    quality = int(form["quality"].value)
    
    if quality < 1:
        quality = 1
    elif quality > 100:
        quality = 100
    
    configuration["quality"] = str(quality)
except ValueError:
    pass

configuration["vertical_flip"] = form["vertical_flip"].value

configuration["horizontal_flip"] = form["horizontal_flip"].value

try:
    timeout = int(form["timeout"].value)
    unit = form["timeout_unit"].value
    
    if unit == "m":
        timeout *= 60
    elif unit == "h":
        timeout *= (60 * 60)
    elif unit == "d":
        timeout *= (60 * 60 * 24)
    
    configuration["timeout"] = str(timeout)
except ValueError:
    pass

configuration["timestamp"] = form["timestamp"].value

with open("settings.conf", "w") as configuration_file:
    parser.write(configuration_file)

print("Content-type: text/html\n" \
      "Location: /cgi/settings.py\n")
