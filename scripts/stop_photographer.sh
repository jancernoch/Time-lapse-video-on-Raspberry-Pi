#!/bin/bash

while IFS=" = " read VARIABLE VALUE
do
    if [[ $VARIABLE != \[*] ]]
    then
        declare "$VARIABLE=$VALUE" 2> /dev/null
    fi
done < settings.conf

PID_FILE="$path/scripts/photographer.pid"

rm -f "$PID_FILE"