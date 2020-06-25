#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from time import sleep

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# This program uses the EV3 speaker and screen to send a message.
# It can be used to test that you were able to send the program to your robot.

# Create your objects here.
msg="Hello El Paso County 4H"
ev3 = EV3Brick()


# Write your program here.
ev3.speaker.beep()
ev3.screen.print(msg)
ev3.speaker.say(msg)

sleep(3.0)
ev3.speaker.say("Good bye")