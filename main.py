import eyes
import _thread
from machine import Pin,I2C

import wifimgr
from time import sleep

import bellyCounter
import earsLED
import servos_main

bus = I2C(0,scl=Pin(21),sda=Pin(22),freq=200000)

###CONNECTION####
# The connection of the matrix display cannot be changed
# VCC to 5.5V
# GND to Ground
# DIN to GPIO13
# CS  to GPIO15
# CLK to GPIO14
#################

def second_thread():

    armIs = "down"
    earsAre = 0
    earsColorIs = "off"

    while True:
        if wifimgr.eyeState == "happy": 
            eyes.displayHappy()
        elif wifimgr.eyeState == "neutral":
            eyes.displayNeutral()
        elif wifimgr.eyeState == "sad":
            eyes.displaySad()
        else:
            print("error, unknown state")
            sleep(10)

        bellyCounter.map_students_to_leds( wifimgr.studentCount)
        
        if wifimgr.arm == "down" and armIs == "up":
            servos_main.move_arm_down()
            armIs = "down"
        if wifimgr.arm == "up" and armIs == "down":
            servos_main.move_arm_up()
            armIs = "up"

        if wifimgr.ears == 0 and earsAre != 0:
            servos_main.ears_default()
            earsAre = 0
        if wifimgr.ears == 1 and earsAre != 1:
            servos_main.ears_half_back()
            earsAre = 1
        if wifimgr.ears == 2 and earsAre != 2:
            servos_main.ears_back()
            earsAre = 2
        if wifimgr.ears == 3 and earsAre != 3:
            servos_main.ears_down()
            earsAre = 3

        if wifimgr.earsColor == "off" and earsColorIs != "off":
            earsLED.disableEars()
            earsColorIs = "off"
        if wifimgr.earsColor == "green" and earsColorIs != "green":
            earsLED.setUserGreen()
            earsColorIs = "green"
        if wifimgr.earsColor == "violet" and earsColorIs != "violet":
            earsLED.setUserViolet()
            earsColorIs = "violet"
        if wifimgr.earsColor == "blue" and earsColorIs != "blue":
            earsLED.setUserBlue()
            earsColorIs = "blue"
        
            

_thread.start_new_thread(second_thread, ())



try:
  import usocket as socket
except:
  import socket

wlan = wifimgr.get_connection()
if wlan is None:
    print("Could not initialize the network connection.")
    while True:
        pass  # you shall not pass :D

# Main Code goes here, wlan is a working network.WLAN(STA_IF) instance.
print("ESP OK")