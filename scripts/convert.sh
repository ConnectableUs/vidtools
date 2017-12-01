#!/bin/bash

# I've built a handbrake from github, it's technically 1.0.7+, but really from master:
# -> HandBrake 20171128162442-c34d437-master
#
# So, for this version, the trick was to use the -Z "CLI Defaults" but set -B manually;
#   - deleting the audio-bit-rate (letting drivers set) still hung; 96 still hung; 48 worked;

CVT=HandBrakeCLI
# everything needed is now in the config json:
OPTS="--preset-import-file hb-audio-fix.json"
FROM_D=Raw_Video
TO_D=MP4_convert


for from in $FROM_D/*.webm; do
    to=$(basename ${from%.*}).m4v
    echo $CVT $OPTS -i "$from" -o "$TO_D/$to"
    $CVT $OPTS -i "$from" -o "$TO_D/$to" 2> convert.log
done

