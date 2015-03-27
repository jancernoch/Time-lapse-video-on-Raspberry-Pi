#!/usr/bin/env python

from configparser import ConfigParser
from os import fork, execv, wait
from os.path import exists



parser = ConfigParser()
parser.read("settings.conf")
configuration = parser["CONFIGURATION"]
path = configuration["path"]
width = configuration["width"]
height = configuration["height"]
quality = configuration["quality"]
vertical_flip = configuration["vertical_flip"]
horizontal_flip = configuration["horizontal_flip"]
timeout = configuration["timeout"]
timestamp = configuration["timestamp"]

print("Content-type: text/html\n")

running = exists(path + "/scripts/photographer.pid")
printing = True

with open(path + "/html/settings.html", "r", encoding="utf8") as file:
    for line in file.readlines():
        if running:
            if "configuration_tag_start" in line:
                printing = False
            elif "configuration_tag_end" in line:
                printing = True
        else:
            if "message_tag_start" in line:
                printing = False
            elif "message_tag_end" in line:
                printing = True
        
        if printing:
            if "running_tag" in line:
                if running:
                    print("<p>Process which takes pictures is running - <a href=\"/cgi/stop.py\">Stop process.</a></p>")
                else:
                    print("<p>Process which takes pictures is not running - <a href=\"/cgi/start.py\">Start process.</a></p>")
            elif "width_tag" in line:
                print("<input class=\"settings\" type=\"text\" name=\"width\" value=\"" + width + "\" />")
            elif "height_tag" in line:
                print("<input class=\"settings\" type=\"text\" name=\"height\" value=\"" + height + "\" />")
            elif "quality_tag" in line:
                print("<input class=\"settings\" type=\"text\" name=\"quality\" value=\"" + quality + "\" />")
            elif "hflip_tag" in line:
                if horizontal_flip == "yes":
                    print("<option value=\"yes\">yes</option>")
                    print("<option value=\"no\">no</option>")
                else:
                    print("<option value=\"no\">no</option>")
                    print("<option value=\"yes\">yes</option>")
            elif "vflip_tag" in line:
                if vertical_flip == "yes":
                    print("<option value=\"yes\">yes</option>")
                    print("<option value=\"no\">no</option>")
                else:
                    print("<option value=\"no\">no</option>")
                    print("<option value=\"yes\">yes</option>")
            elif "timeout_tag" in line:
                print("<input class=\"settings\" type=\"text\" name=\"timeout\" value=\"" + timeout + "\" />")    
            elif "timestamp_tag" in line:
                if timestamp == "yes":
                    print("<option value=\"yes\">yes</option>")
                    print("<option value=\"no\">no</option>")
                else:
                    print("<option value=\"no\">no</option>")
                    print("<option value=\"yes\">yes</option>")
            else:
                print(line, end="")
