# Time-lapse-video-on-Raspberry-Pi

This is the set of scripts which are able to collect pictures in defined time interval from camera on Raspberry Pi and create time-lapse video from them. Every features of this scripts should be controlled by the web interface.



Dependencies:

Raspberry Pi with camera module (+ official software for taking pictures - "raspistill")

Http server with CGI support (e.g. Lighttpd or Apache)

Python 3

FFMPEG

Imagemagick



Instalation:

1. Install and configure any http server with CGI (Python 3) support.

2. Move all files into http "home" directory.

3. Change "path" in settings.conf file.
