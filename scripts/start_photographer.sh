#!/bin/bash

while IFS=" = " read VARIABLE VALUE
do
    if [[ $VARIABLE != \[*] ]]
    then
        declare "$VARIABLE=$VALUE" 2> /dev/null
    fi
done < settings.conf

if [[ $horizontal_flip = "yes" ]]
then
    horizontal_flip="-hf"
else
    horizontal_flip=""
fi

if [[ $vertical_flip = "yes" ]]
then
    vertical_flip="-vf"
else
    vertical_flip=""
fi

echo $timestamp

PID_FILE="$path/scripts/photographer.pid"

if [ -f "$PID_FILE" -a $(cat "$PID_FILE") = "$$" ]
then
    exit 0
fi

echo $$ > "$PID_FILE"

while [ -f "$PID_FILE" -a $(cat "$PID_FILE") = "$$" ]
do
    DATE=$(date +"%d.%m.%Y %H:%M:%S %Z")
    FILENAME=$(echo "$DATE" | sed -e "s/[\.:]/_/g" -e "s/ /__/g")
    FILENAME="$FILENAME.jpg"

    raspistill -w "$width" -h "$height" -q "$quality" $horizontal_flip $vertical_flip -o "$path/data/$FILENAME"
    
    if [[ $timestamp = "yes" ]]
    then
        convert -pointsize 20 -gravity southeast -fill yellow -annotate +10+10 " $DATE " "$path/data/$FILENAME" "$path/data/$FILENAME"
    fi
    
    sleep "$timeout"
done
