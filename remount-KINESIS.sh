#!/bin/sh
#
# This works around bug where, by default, macOS 14.x writes part of a file 
# immediately, and then doesn't update the directory for 20-60 seconds, causing
# the file system to be corrupted.
#

disky=`df | grep KINESIS | cut -d" " -f1`
sudo umount /Volumes/KINESIS
sudo mkdir /Volumes/KINESIS
sleep 2
sudo mount -v -o noasync -t msdos $disky /Volumes/KINESIS