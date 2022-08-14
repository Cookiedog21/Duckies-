#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)


robot = DriveBase(left_motor, right_motor, wheel_diameter=95, axle_track=140)
# Go forward and backwards for one meter.
robot.straight(1000)
ev3.speaker.beep()


# Write your program here.
ev3.speaker.beep()
robot.straight(-1000)



# Write your program here.
ev3.speaker.beep()


