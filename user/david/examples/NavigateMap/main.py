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

ARM_SPEED = 500
ARM_MAX_ANGLE = 3200
ARM_MIN_ANGLE = 0
DRIVE_SPEED = 50
DRIVE_SLOW_SPEED = 10

# Create your objects here.
ev3 = EV3Brick()

# Initialize the motors.
leftMotor = Motor(Port.B)
rightMotor = Motor(Port.C)

# Initialize the drive base.
robot = DriveBase(leftMotor, rightMotor, wheel_diameter=55.5, axle_track=104)

# Initialize the arm motor
armMotor = Motor(Port.A)

# Initialize the Touch Sensor. It is used to detect when the arm motor has
# opened all the way.
touchSensor = TouchSensor(Port.S4)

# Initialize the color sensor. It is used to detect the color of the ground.
colorSensor = ColorSensor(Port.S1)

# Initialize the gyro sensor.
gyroSensor = GyroSensor(Port.S2)

# Initialize the ultrasonic sensor.
ultraSensor = UltrasonicSensor(Port.S3)

# Set a variable that can be used to stop the program if needed.
running = True

# Write your program here.

def stopRobot():
    running = False
    robot.stop()
    armMotor.stop()
    ultraSensor.distance(silent=True)

# Send a message and stop the program
def error(msg):
    stopRobot()
    ev3.light.on(Color.RED)
    ev3.screen.print(msg)
    ev3.speaker.beep(frequency=500, duration=500)
    sleep(1.0)
    ev3.speaker.say(msg)

# Start the the robot and run some initial steps.
#     Calibrate the arm motor
#     Drive strait until the color sensor detects a non-yellow color.
def start():
    while (running and not touchSensor.pressed()):
        armMotor.run(ARM_SPEED)
    armMotor.reset_angle(ARM_MAX_ANGLE)
    armMotor.run_target(ARM_SPEED, ARM_MIN_ANGLE, then=Stop.HOLD, wait=False)

    ev3.speaker.play_file(SoundFile.SPEED_UP)

    while (running and colorSensor.color() == Color.YELLOW):
        robot.drive(100, 0)

# Follow the right side of a black line with a green background
def followBlackLine():
    robot.reset()
    turnRate = 60
    while (running):
        color = colorSensor.color()
        if (color == Color.BLACK):
            robot.drive(DRIVE_SPEED, turnRate)
        elif (color == Color.GREEN):
            robot.drive(DRIVE_SPEED, -turnRate)
        else:
            colorStr = "None"
            if (color != None):
                colorStr = "{}".format(color).replace("Color.", "")
            robot.drive(DRIVE_SLOW_SPEED, 0)
            #error("Color {} not recognized in follow black line.".format(colorStr))
            #break

start()
followBlackLine()

stopRobot()