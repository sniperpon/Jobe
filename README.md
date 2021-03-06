# Jobe
Contains the code for the Jobe robot lawn mower driver program.

This is on hiatus at the moment; the camera image processing is going to be substantially more difficult than I'd imagined, to a prohibitive degree. Will need to find a different solution. Beyond that, my new riding mower is so efficient that I'm not certain there is a purpose to this project any longer.

### Phases
* Camera code
    * ~~Get Github repository and IDEA set up~~
    * ~~Write pygame code simulator, with stubbed out modules~~
    * ~~Get basic Python code running on Raspberry Pi~~
    * ~~Time-boxed rewrite of simulator using only sprites~~
    * ~~Write preliminary AI~~
    * Implement camera module, with image detection logic

* Wheel motor code
    * Buy motor controllers
    * Order motors and wheels
    * Connect motor controller to wheels and Pi
    * ~~Implement code to send signals to motor controller~~

* Assembly
    * Buy alternator and battery
    * Physically hook wheels and electronics to mower frame
    * Hook alternator to engine, connect to battery
    * Connect battery to motor controllers
    * Debug and revise code


### Frame
* Replace front and rear wheels and axles with motors and new wheels
* Create a lever that will lock choke mechanism to "on" position
* Bolt alternator to mower frame
* Secure battery to frame
* Secure water-proof electronics box to frame, with camera angled properly
* Connect battery to motor controllers
* [Hook](https://theepicenter.com/blog/generator-lawn-mower-vertical/) alternator to engine and battery


### Misc Notes
* To get virtualenv created:
    * sudo apt-get install python-opencv
    * sudo apt-get install virtualenvwrapper
    * sudo apt-get install python2-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsdl1.2-dev libsmpeg-dev python-numpy subversion libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev
    * Add snippet to .bashrc file, source .bashrc
    * workon
    * mkdir .virtualenv
    * cd .virtualenv
    * virtualenv -p /usr/bin/python2 jobe
    * workon jobe
    * pip install jobe
* [Here](https://makemypi.wordpress.com/2016/12/19/remote-debug-on-raspberry-pi-by-pycharm/) is how to get remote debugging working
    * Only supported in [Ultimate Edition](https://www.jetbrains.com/idea/buy/#edition=personal)
* Helpful pygame example sprite code [here](http://thepythongamebook.com/en:pygame:step014)
* Need
    * [ThunderBorg x2](https://www.piborg.org/thunderborg/thunderborg) = $96.44
    * [Motor plus wheel x4](https://www.piborg.org/accessories/12v-motor) = $93.80
    * [Cables x8, half red, half black](https://www.piborg.org/accessories/wire-22awg-red) = $7.82
    * [Batteries](http://www.robotmarketplace.com/products/batteries_main.html) = $75
    * Total: $273.06
* OpenCV Links
    * [Canny edge detection](http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_canny/py_canny.html)
    * [Bounding boxes](http://www.learnopencv.com/how-to-select-a-bounding-box-roi-in-opencv-cpp-python/)
    * [FAST feature detection](http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_fast/py_fast.html)
* [Backup](https://thepihut.com/blogs/raspberry-pi-tutorials/17789160-backing-up-and-restoring-your-raspberry-pis-sd-card) SD card
    * [Another](https://www.raspberrypi.org/documentation/linux/filesystem/backup.md) link


### Already Existing
* Husqvarna: $1999.95 just to get in the door
* LawnBott: Also $2000+ to get in the door
* [Summary](http://www.toptenreviews.com/home/outdoor/best-robot-lawn-mowers/)
