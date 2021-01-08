#!/bin/bash
sleep 5 # wait for ui to finalize starting up
# If running on xorg: scrot
# Otherwise, probably compatible with grim
touch /vagrant/screenshots/$DE_NAME # TODO take screenshot
echo "OK" | nc -nc 127.0.0.1 1042
