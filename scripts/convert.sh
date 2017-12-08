#!/bin/bash

# I've built a handbrake from github, it's technically 1.0.7+, but really from master:
# -> HandBrake 20171128162442-c34d437-master
#
# So, for this version, the trick was to use the -Z "CLI Defaults" but set -B manually;
#   - deleting the audio-bit-rate (letting drivers set) still hung; 96 still hung; 48 worked;

CVT=HandBrakeCLI
# everything needed is now in the config json:
# hb-audio-match based on -Z Normal and manually matching audio bitrate of sources
OPTS="--preset-import-file hb-audio-match.json"
OPTS="-B 16 -O -I"

FROM_D=original_videos
TO_D=mp4_converted

for from in $FROM_D/*.webm; do
    to=$(basename ${from%.*}).mp4
    echo $CVT $OPTS -i "$from" -o "$TO_D/$to": | tee $TO_D/convert.log
    $CVT $OPTS -i "$from" -o "$TO_D/$to" 2>> $TO_D/convert.log
done

