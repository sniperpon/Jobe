# Jobe
Contains the code for the Jobe robot lawn mower driver program

### Phases
* Camera code
    * ~~Get Github repository and IDEA set up~~
    * ~~Write pygame code simulator, with stubbed out modules~~
    * ~~Get basic Python code running on Raspberry Pi~~
    * Time-boxed rewrite of simulator using only sprites
    * Implement camera module, with image detection logic

* Wheel motor code
    * Buy lawn mower and wheel chair
    * Order motor controller
    * Remove wheels, connect to motor controller, to Raspberry Pi
    * Implement code to send signals to motor controller

* Assembly
    * Buy alternator
    * Hook wheels and electronics to mower frame
    * Hook alternator to engine, connect to motor controller
    * Debug and revise code


### Code
* Go forward until sees short grass, use [bytes](https://docs.python.org/3/library/stdtypes.html#bytes) in Python to control motors
* Run forward according to overlap variable
* Turn 90 degrees to the left by having right wheel move, left wheel stopped
* Go forward, constantly adjusting to stay inline with mowed grass on the right


### Controls
* Put Raspberry Pi into control box
* Put Sabertooth [into](https://www.amazon.com/Sabertooth-Dual-25A-Motor-Driver/dp/B008OMQUXC?SubscriptionId=AKIAILSHYYTFIVPWUY6Q&tag=duckduckgo-d-20&linkCode=xm2&camp=2025&creative=165953&creativeASIN=B008OMQUXC) control box
* [Hook](https://www.raspberrypi.org/learning/getting-started-with-picamera/) Pi Camera to Raspberry Pi (camera port)
* Hook Sabertooth to components
    * [Alternator](https://www.amazon.com/Electrical-ADR0152-Self-Excited-90-01-3125S-70-01-7127SE/dp/B0081S9C16) (12V one wire)       
    * [Raspberry Pi](https://www.raspberrypi.org/forums/viewtopic.php?f=37&t=12067) (5V, GPIO headers)
        * Another [source](https://www.youtube.com/watch?v=QCNoVRgETRc)                                  
    * [Motors](https://www.youtube.com/watch?v=ruHEJGudIjs) (motor wires)
        * Another [source](https://www.intorobotics.com/2-simple-methods-choose-motors-wheel-drive-robots/)
* [Hook](https://www.youtube.com/watch?v=ruHEJGudIjs?t=3m32s) Alternator to mower engine


### Frame
* Mount 1 inch bars to existing lawn mower frame
* Create a lever that will lock choke mechanism to "on" position
* Connect 90 degree-capable wheels to bars
* Hook one servo moter to each of the wheels
* Bolt alternator to mower frame
* Connect water-proof control box to frame
* Mount camera to frame
* [Hook](https://theepicenter.com/blog/generator-lawn-mower-vertical/) alternator to motor


### Misc Notes
* To get virtualenv created:
    * sudo apt-get install virtualenvwrapper
    * sudo apt-get install python3-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsdl1.2-dev libsmpeg-dev python-numpy subversion libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev
    * Add snippet to .bashrc file, source .bashrc
    * workon
    * mkdir .virtualenv
    * cd .virtualenv
    * virtualenv -p /usr/bin/python3 jobe
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


### Already Existing
* Husqvarna: $1999.95 just to get in the door
* LawnBott: Also $2000+ to get in the door
* [Summary](http://www.toptenreviews.com/home/outdoor/best-robot-lawn-mowers/)