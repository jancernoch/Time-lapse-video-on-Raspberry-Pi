#!/bin/bash

while IFS=" = " read VARIABLE VALUE
do
    if [[ $VARIABLE != \[*] ]]
    then
        declare "$VARIABLE=$VALUE" 2> /dev/null
    fi
done < settings.conf

PID_FILE="$path/scripts/converter.pid"

if [ -f "$PID_FILE" -a $(cat "$PID_FILE") = "$$" ]
then
    exit 0
fi

echo $$ > "$PID_FILE"

ffmpeg -y -i "$path/data/image_%08d.jpg" -vcodec libx264 "$path/video.mp4"

rm -f $path/data/image_*.jpg
rm -f "$PID_FILE"
