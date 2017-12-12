#!/bin/bash
# -- for use w/ single, or a few files
for i in "$@"; do
    ffmpeg -i "$i" 2>&1 | grep Duration | cut -d ' ' -f 4 | sed s/,//
done
