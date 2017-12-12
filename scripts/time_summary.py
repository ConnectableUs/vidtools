#!/usr/bin/env python
# coding: utf-8
'''
pipeline filter (reads stdin)
use with video_durations.sh, e.g.:

    video_durations.sh original_videao | time_summary.py

Alternatively:

    video_durations.sh original_videao > foo.txt
    time_summary.py < foo.txt

The line format from video_durations.sh (uses ffmpeg) is currently this:

    Rec11-13-2017_10-02-38.mp4  Duration: 00:31:12.96, start: 0.104000, bitrate: 83 kb/s

Any lines ending in punctuation are ignored.
Assumes python3.5 minimum;  If you're not using it, you get what you deserve...
'''
import sys
import string

if sys.version_info.major < 3 \
   or (sys.version_info.minor < 5 and sys.version_info.major == 3):
    print(__doc__)
    sys.exit(1)

# with open('durations.mp4_converted.txt', 'r') as f:
#    data = f.readlines()
# rather run this in a pipeline:

# ignore any leading header lines:
#  ffmpeg Durations output lines end in "kb/s",
#  so lets quash any lines ending in non alpha:
#   (considered: doing instead for lines starting w/ "#")
vid_times = []
for line in sys.stdin:
    # ignore header lines (lines ending in newline)
    if line[-2] in string.punctuation:
        continue
    # extract the "HH:MM:SS.ss" info (kill the trailing comma)
    time_str = line.split()[2][:-1]
    # now split the "HH:MM:SS.ss" string
    #  want to split the fractional second too, so
    vid_time = time_str.replace('.',':').split(':')
    vid_times.append([int(i) for i in vid_time])

# at this point, we have: HH, MM, SS, decaS in str format
# Now sum the columns, and do the overflow:
sum_times = [ sum([time[i] for time in vid_times]) for i in range(len(vid_times[0])) ]

# sum_times has simple summed: [H, M, S, dS]
# simplify by carrying up:
sum_times.reverse()  # deal w/ LS=> MS quantities
div = 100  # only first time: for dS
carry = 0  # initial carry value
for i, v in enumerate(sum_times):
    carry, newv = divmod(v+carry, div)
    div = 60  # each time, except first
    sum_times[i] = newv
sum_times.reverse()  # ready to display result in H:M:S:dS order

print(f"Total video length: "
      f" {sum_times[0]}h {sum_times[1]}m {sum_times[2]}.{sum_times[3]}s")
