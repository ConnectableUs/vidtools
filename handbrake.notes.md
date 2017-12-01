# handbrake

It turns out that the "libav aac" audio encoder is the problem.
A solution is to use a non-open-source aac encoder, the fdk-aac.
This should build functional handbrake instances:

    `./configure --launch-jobs=4 --enable-fdk-aac --launch`

I leave the rest, below, for completeness.

- for Ubuntu, handbrake `0.10.2+` sort of worked;
- apt uninstalled the GUI version, and updated to a (broken) version
  of `HandBrakeCLI` 1.04;
- looking for alternatives, I tried / installed `ffmulticonverter`, apparently
  a python script driver for ffmpeg;  very slow, and large resultant files;
- I tried `ffmpeg` directly - broke on the 5 problem files; otherwise, large output;
  - looked at [http://www.bugcodemaster.com/article/convert-videos-mp4-format-using-ffmpeg]
  - looked at [https://trac.ffmpeg.org/wiki/Encode/H.264], two-pass and some presets examples

- finally cloned repo for handbrake: [https://github.com/HandBrake/HandBrake]
  - to build, see hints at: [https://www.packtpub.com/books/content/compiling-and-running-handbrake-ubuntu]
  - some notes:
    - I went around a long way, but suggest you just follow these:
      https://handbrake.fr/docs/en/latest/developer/install-dependencies-ubuntu.html
    - for linux build, include `--enable-fdk-aac` in your ./configure, e.g.:
      `./configure --launch-jobs=4 --enable-fdk-aac --launch`

  - historical (unecessarily long) process notes:
    - installed:
      - `sudo apt install yasm`
      - `sudo apt install intltool`
      - For finding HandBrakeCLI, did make -p (the tag was "HandBrakeCLI");
      - `sudo apt install libmp3lame-dev`
      - `sudo apt install libopus-dev`
      - `sudo apt install libx264-dev`

    - finally ran into these:
      - [https://handbrake.fr/docs/en/latest/developer/install-dependencies-gentoo.html]
      - `sudo apt install libsamplerate0-dev`
      - `sudo apt install libtheora-dev`

    - didn't follow these yet, but here they are:
      - [https://handbrake.fr/docs/en/latest/developer/install-dependencies-ubuntu.html]
      - [https://handbrake.fr/docs/en/latest/developer/build-linux.html]

    - did just copy / paste the ubuntu dependency lines; only the gui lines installed anything;

