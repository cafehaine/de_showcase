#!/bin/bash
sleep 5 # wait for ui to finalize starting up
scrot "/vagrant/screenshots/${DE_NAME}.png" || grim "/vagrant/screenshots/${DE_NAME}.png"
echo "OK" | nc -nc 127.0.0.1 1042
