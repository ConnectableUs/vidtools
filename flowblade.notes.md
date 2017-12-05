# Installing flowblade

Flowblade gets a lot of
[good press](https://opensource.com/life/16/9/10-reasons-flowblade-linux-video-editor),
and is laregely / only a python solution, albeit using python-2.

It claims to run under Ubuntu 16.04, but this seems to depend on the Ubuntu
installed python-2.7.12 and access to supporting libraries.  I tried installing to use
a self-built & installed python-2.7, but could not successfully install the MLT python interface.
The system python-2.7 didn't seem to have a problem with that.

Here's some fundamental notes:

- basic [installation instructions](https://github.com/jliljebl/flowblade/blob/master/flowblade-trunk/docs/INSTALLING.md)
- additional steps:
  - edit the startup script, so that it uses the Ubuntu installed python-2.7:
  ```
  # set top line to #!/usr/bin/python2
  $ sudo vi $(which flowblade)
  ```
  - upon running, install any missing python dependencies (I needed to install `mumpy`):
      ```
      $ /usr/bin/python2 -m pip install -U numpy
      ```

That seems to make for a functioning *flowblade* - not sure what type of project to create, yet (reading docs).

