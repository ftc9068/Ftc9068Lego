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


# Create your objects here.
ev3 = EV3Brick()

# Documentation on these classes can be found by clicking on the Lego Mindstorm EV3 Micropython
# extension and then Open user guide. Expand the EV3 devices and click on the sensor you want to
# look up.
colorSensor = ColorSensor(Port.S1)
gyroSensor = GyroSensor(Port.S2)
ultraSensor = UltrasonicSensor(Port.S3)
touchSensor = TouchSensor(Port.S4)




# Write your program here.
ev3.speaker.beep()
gyroSensor.reset_angle(0)


# Clear the screen and set the text that does not change.
ev3.screen.clear()
#ev3.screen.set_font(font)
ev3.screen.draw_text(0, 0, "Sensor Values", text_color=Color.BLACK, background_color=None)
ev3.screen.draw_text(10, 18, "Color: ", text_color=Color.BLACK, background_color=None)
ev3.screen.draw_text(10, 36, "Gyro: ", text_color=Color.BLACK, background_color=None)
ev3.screen.draw_text(10, 54, "Ultra Sonic: ", text_color=Color.BLACK, background_color=None)
ev3.screen.draw_text(10, 72, "Touch: ", text_color=Color.BLACK, background_color=None)

colorValue = ""
gyroValue = ""
ultraValue = ""
touchValue = ""

keepRunning = True
while keepRunning:
    previousColorValue = colorValue
    colorValue = "{}".format(colorSensor.color()).replace("Color.", "")
    if (colorValue != previousColorValue):
        ev3.screen.draw_text(70, 18, previousColorValue, text_color=Color.WHITE, background_color=Color.WHITE)
        ev3.screen.draw_text(70, 18, colorValue, text_color=Color.BLACK, background_color=Color.WHITE)

    previousGyroValue = gyroValue
    gyroValue = "{}".format(gyroSensor.angle())
    if (gyroValue != previousGyroValue):
        ev3.screen.draw_text(120, 36, previousGyroValue, text_color=Color.WHITE, background_color=Color.WHITE)
        ev3.screen.draw_text(120, 36, gyroValue, text_color=Color.BLACK, background_color=Color.WHITE)

    previousUltraValue = ultraValue
    ultraValue = "{}".format(ultraSensor.distance())
    if (ultraValue != previousUltraValue):
        ev3.screen.draw_text(120, 54, previousUltraValue, text_color=Color.WHITE, background_color=Color.WHITE)
        ev3.screen.draw_text(120, 54, ultraValue, text_color=Color.BLACK, background_color=Color.WHITE)

    previousTouchValue = touchValue
    touchValue = "{}".format(touchSensor.pressed())
    if (touchValue != previousTouchValue):
        ev3.screen.draw_text(120, 72, previousTouchValue, text_color=Color.WHITE, background_color=Color.WHITE)
        ev3.screen.draw_text(120, 72, touchValue, text_color=Color.BLACK, background_color=Color.WHITE)

    keepRunning = not Button.CENTER in ev3.buttons.pressed()
    sleep(0.1)




colorSensor.ambient()
ultraSensor.distance(silent=True)


ev3.speaker.say("Goodbye")
