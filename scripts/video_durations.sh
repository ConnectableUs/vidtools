#/bin/bash

# measure by directory
DIRNAME=${1:-mp4_converted}
EXT=${2:-mp4}

echo $DIRNAME:

for i in $DIRNAME/*; do
    # only look at files with EXT extension
    [ "${i##*.}" = "$EXT" ] || continue
    ffmpeg -i "$i" 2>&1 | { echo -n ${i##*/}; fgrep Duration; }
done
