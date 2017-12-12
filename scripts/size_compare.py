#!/usr/bin/env python
# coding: utf-8
import os
import sys

if len(sys.argv) != 3:
    # could write this as:
    # sys.argv[0][sys.argv[0].rindex('/')+1:]
    script_name = sys.argv[0]
    try:
        base = script_name.rindex('/')+1
    except:
        base = 0
    script = script_name[base:]
    msg = f'''two arguments required.
    Usage:
      {script} dir1 dir2

      shows size of files in each  directory
      filename extension can differ between direcories,
        but must be uniform in a directory

      Files removed from comparison:
          README.txt
          convert.log
    Assumptions:
        python 3.5 minimum (fstrings)
    '''
    print(msg, file=sys.stderr)
    sys.exit(1)


dir1_n = sys.argv[1]
dir1 = os.listdir(dir1_n)

dir2_n = sys.argv[2]
dir2 = os.listdir(dir2_n)

l = max(len(dir1_n), len(dir2_n)) + 4

print(f"{dir1_n}  vs  {dir2_n}  file sizes\n------")

for i in dir1, dir2:
    try:
        i.remove('README.txt')
        i.remove('convert.log')
    except:
        pass
    i.sort()

# extension lengths - assumes uniform extension names:
# index of the core name (the name w/o extension)
# core_i = lambda n: n.rindex('.') if n else 0

def core_i(name):
    try:
        return name.rindex('.')
    except:
        return 0

# set baseline extensions:
dir1_e = dir1[0][core_i(dir1[0]):]
dir2_e = dir2[0][core_i(dir2[0]):]

# set operations on dir lists:
def d_set(l):
    '''returns a set of core-names from list l'''
    core = core_i(l[0])  # assume all extensions alike
    return {x[:core] for x in l}

# if the file names differ in the two directories:
set_dir1, set_dir2 = d_set(dir1), d_set(dir2)

def show_diff(name, dif):
    ''' show the exclusive file list in dir name'''
    print(f"only in {name}:")
    for i in dif:
        print(f"{name}/{i}")

if set_dir1 ^ set_dir2:
    dif = set_dir1 - set_dir2
    if dif:
        show_diff(dir1_n, dif)
    dif = set_dir2 - set_dir1
    if dif:
        show_diff(dir2_n, dif)


l1 = len(dir1)
l2 = len(dir2)
longest = l1 if max(l1, l2) == l1 else l2
dir_longest, dir_longest_n = (dir1, dir1_n) if longest == l1 \
                        else (dir2, dir2_n)


def get_name(dir, i):
    ''' given a dir list, and an index, return a matching name'''
    if dir == dir_longest:
        return dir[i]
    else:
        # core_name of dir_longest + extension of dir
        ext = dir1_e if dir is dir1 else dir2_e
        j = core_i(dir_longest[i])
        if dir_longest[i][:j]+ext in dir:
            return dir[i]
        else:
            return ""

d1_total = d2_total = 0
for i in range (longest):
    d1_f = get_name(dir1, i)
    d2_f = get_name(dir2, i)
    c1 = core_i(d1_f)
    c2 = core_i(d2_f)
    d1_s = os.stat(os.path.join(dir1_n, d1_f)).st_size
    d2_s = os.stat(os.path.join(dir2_n, d2_f)).st_size
    print(f"{d1_f[:c1]}: {d1_s:10,} ({d1_f[c1+1:]}) <= {d2_s:10,} ({d2_f[c2+1:]})")
    d1_total += d1_s
    d2_total += d2_s

print(f"\n{dir1_n:{l}} total: {d1_total:12,} ({d1_f[c1+1:]})\n{dir2_n:{l}} total: {d2_total:12,} ({d2_f[c2+1:]})")


