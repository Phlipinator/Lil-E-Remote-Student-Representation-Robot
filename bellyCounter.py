from machine import Pin
from neopixel import NeoPixel
from time import sleep

#######CONNECTION#######
# DATA: Green, Pin 16
# GND: White
# VCC: Grey
########################

def map_students_to_leds(number_of_students, color = (255,255,255)):
    np = NeoPixel(Pin(16), 12)
    
    # choose correct leds
    if number_of_students == 0:
        adressed = []
    elif number_of_students == 1:
        adressed = [0,1,11]
    elif number_of_students > 1 and number_of_students <= 2:
        adressed = [0,1,2,10,11]
    elif number_of_students > 2 and number_of_students <= 3:
        adressed = [0,1,2,3,9,10,11]
    elif number_of_students > 3 and number_of_students <= 4:
        adressed = [0,1,2,3,4,8,9,10,11]
    elif number_of_students >= 4:
        adressed = range(12)

    # turn all leds off
    for i in range(12):
                np[i] = (0, 0, 0)
                np.write()

    # apply color
    for i in adressed:
                np[i] = color
                np.write()


def empty_avatar(color = (255,255,255)):
    np = NeoPixel(Pin(14), 12)
    
    # turn all leds off
    for i in range(12):
                np[i] = (0, 0, 0)
                np.write()
                
def half_avatar(color = (255,255,255)):
    np = NeoPixel(Pin(14), 12)   
    
    adressed = [0,1,2,3,9,10,11]

    # turn all leds off
    for i in range(12):
                np[i] = (0, 0, 0)
                np.write()

    # apply color to chosen leds
    for i in adressed:
                np[i] = color
                np.write()

def few_avatar(color = (255,255,255)):
    np = NeoPixel(Pin(14), 12)   
    adressed = [0,1,2,10,11]

    # turn all leds off
    for i in range(12):
                np[i] = (0, 0, 0)
                np.write()

    # apply color to chosen leds
    for i in adressed:
                np[i] = color
                np.write()

def one_avatar(color = (255,255,255)):
    np = NeoPixel(Pin(14), 12)   
    adressed = [0,1,11]

    # turn all leds off
    for i in range(12):
                np[i] = (0, 0, 0)
                np.write()

    # apply color to chosen leds
    for i in adressed:
                np[i] = color
                np.write()
                
def many_avatar(color = (255,255,255)):
    np = NeoPixel(Pin(14), 12)   
    adressed = [0,1,2,3,4,8,9,10,11]

    # turn all leds off
    for i in range(12):
                np[i] = (0, 0, 0)
                np.write()

    # apply color to chosen leds
    for i in adressed:
                np[i] = color
                np.write()
                
def full_avatar(color = (255,255,255)):
    np = NeoPixel(Pin(14), 12)   

    # apply color to chosen leds
    for i in range(12):
                np[i] = color
                np.write()
