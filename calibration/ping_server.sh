#!/bin/bash

server="curl https://calibrationoftools.shauryayamdagn1.repl.co"

while true; do
    curl $server > /dev/null
    #ping -c 1 $server > /dev/null

    if [ $? -eq 0 ]; then
        echo "Server is online."
    else
        echo "Server is offline."
    fi

    sleep 60  # Wait for 2 minutes before pinging again
done

