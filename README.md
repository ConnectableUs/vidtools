# vidtools - video conversion tools and setup

This tracks open source video tools, and sets working configurations.

Currently component builds and configurations:

## HandBrake (cloned)

Initially, a working version was tagged PP-build.
It turns out that the problem is with the libav aac audio encoder.
Building w/ an alternative (better) encoder solves the problem (see handbrake.notes.md, and forum post).

  - for build configuration notes, see: `handbrake.notes.md`
  - `convert.sh` shell script is primitive, but working; will update as need arises;
  - current working settings in `hb-audio-fix.json`;
  - discussion about hanging issue: [handbrake forum topic](https://forum.handbrake.fr/viewtopic.php?f=13&t=37151&p=175283#p175283)

## flowblade installed on Ubuntu

See the [flowblade.notes.md]() document.
