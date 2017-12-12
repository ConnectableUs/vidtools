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

Assumes python3.5 minimum;  If you're not using it, you get what you deserve...
'''
import sys

#with open('durations.mp4_converted.txt', 'r') as f:
#    data = f.readlines()
## rather run this in a pipeline:
data = sys.stdin.readlines()

# strip newlines
data = [ i[:-1] for i in data ]
# extract the HH:MM:SS.ss  info
length_str = [ v.split()[2][:-1] for v in data ]

# convert to summable integer fields: (HH, MM, SS, MS)
# - first step gets to HH, MM, SS.ss:
vid_length = [ v.split(':') for v in length_str ]
vid_time = [ i[:-1] for i in vid_length ]

for i in range(len(vid_time)):
    # split the seconds into seconds and fractional seconds
    vid_time[i].extend(vid_length[i][-1].split('.'))

# at this point, we have: HH, MM, SS, decaS in str format
# Now sum the columns, and do the overflow:
sum_times = [ sum([int(i[j]) for i in vid_time]) for j in range(len(vid_time[0])) ]

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

print(f"Total video length: {sum_times[0]}h {sum_times[1]}m {sum_times[2]}.{sum_times[3]}s")

