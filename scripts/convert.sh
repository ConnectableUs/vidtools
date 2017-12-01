#!/bin/bash
set +x

# This is now old:
#HandBrakeCLI -Z "Normal" -O -I -i Rec11-13-2017_10-02-38.webm -o MP4/Rec11-13-2017_10-02-38.m4v 2> MP4/hbcli.log

# I've built a handbrake from github, it's technically 1.0.7+, but really from master:
# -> HandBrake 20171128162442-c34d437-master
#
# So, for this version, the trick was to use the -Z "CLI Defaults" but set -B manually;
#   - deleting the audio-bit-rate (letting drivers set) still hung; 96 still hung; 48 worked;

CVT=HandBrakeCLI
# cannot have "-Z Normal" for an option:  the -b 160 hangs on 5 videos;
# OBSOLETE: --> instead, do this:
#NORMAL="-e x264 -q 20.0 -E ffaac -6 dpl2 -R Auto -D 0.0 --audio-copy-mask aac,ac3,dtshd,dts,mp3 --audio-fallback ffac3 -f mp4 --loose-anamorphic --modulus 2 -m --x264-preset veryfast --h264-profile main --h264-level 4.0"
#OPTS="-O -I"
# everything needed is now in the config json:
OPTS="--preset-import-file hb-yarkos.json"
FROM_D=
TO_D=$HOME/Videos


for from in $FROM_D/*.webm; do
    to=$(basename ${from%.*}).m4v
    echo $CVT $OPTS -i "$from" -o "$TO_D/$to"
    $CVT $OPTS -i "$from" -o "$TO_D/$to" 2> convert.log
done

