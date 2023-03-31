from machine import Pin, SPI
from max7219 import Max7219
import time

# Initialisation
spi = SPI(1, baudrate=10000000)
screen = Max7219(16, 8, spi, Pin(15))

fixation = 5
blinkTime = 0.4
animation = 0.05
    

    
def displayHappy():
    happyOne()
    time.sleep(fixation)
    happyTwo()
    time.sleep(animation)
    happyThree()
    time.sleep(animation)
    blink()
    time.sleep(blinkTime)
    happyThree()
    time.sleep(animation)
    happyTwo()
    time.sleep(animation)
    happyOne()
    
    time.sleep(2 * animation)
    happyTwo()
    time.sleep(animation)
    happyThree()
    time.sleep(animation)
    blink()
    time.sleep(blinkTime)
    happyThree()
    time.sleep(animation)
    happyTwo()
    time.sleep(animation)
    happyOne()
    
def displayNeutral():
    
    neutralOne()
    time.sleep(fixation)
    neutralTwo()
    time.sleep(animation)
    neutralThree()
    time.sleep(animation)
    blink()
    time.sleep(blinkTime)
    neutralThree()
    time.sleep(animation)
    neutralTwo()
    time.sleep(animation)
    neutralOne()
    
    time.sleep(2 * animation)
    neutralTwo()
    time.sleep(animation)
    neutralThree()
    time.sleep(animation)
    blink()
    time.sleep(blinkTime)
    neutralThree()
    time.sleep(animation)
    neutralTwo()
    time.sleep(animation)
    neutralOne()
    
def displaySad():
    
    sadOne()
    time.sleep(fixation)
    sadTwo()
    time.sleep(animation)
    sadThree()
    time.sleep(animation)
    blinkSad()
    time.sleep(blinkTime)
    sadThree()
    time.sleep(animation)
    sadTwo()
    time.sleep(animation)
    sadOne()
    
    time.sleep(2 * animation)
    sadTwo()
    time.sleep(animation)
    sadThree()
    time.sleep(animation)
    blinkSad()
    time.sleep(blinkTime)
    sadThree()
    time.sleep(animation)
    sadTwo()
    time.sleep(animation)
    sadOne()
     
def blink():
    screen.fill(0)
    
    screen.hline(1,4,6,1)
    screen.hline(9,4,6,1)
    
    screen.show()

def blinkSad():
    screen.fill(0)
    
    screen.hline(1,3,6,1)
    screen.hline(9,3,6,1)
    
    screen.show()
    
def happyOne():
    screen.fill(0)
    
    screen.vline(0,3,2,1)
    screen.vline(7,3,2,1)
    screen.hline(2,1,4,1)
    screen.pixel(1,2,1)
    screen.pixel(6,2,1)
    
    screen.vline(8,3,2,1)
    screen.vline(15,3,2,1)
    screen.hline(10,1,4,1)
    screen.pixel(9,2,1)
    screen.pixel(14,2,1)
    
    screen.show()
    
def happyTwo():
    screen.fill(0)
    
    screen.vline(0,3,2,1)
    screen.vline(7,3,2,1)
    screen.hline(3,1,2,1)
    screen.hline(1,2,2,1)
    screen.hline(5,2,2,1)
  
    screen.vline(8,3,2,1)
    screen.vline(15,3,2,1)
    screen.hline(11,1,2,1)
    screen.hline(9,2,2,1)
    screen.hline(13,2,2,1)
 
    screen.show()
    
def happyThree():
    screen.fill(0)
    
    screen.pixel(0,4,1)
    screen.pixel(7,4,1)
    screen.hline(3,2,2,1)
    screen.hline(1,3,2,1)
    screen.hline(5,3,2,1)
    
    screen.pixel(8,4,1)
    screen.pixel(15,4,1)
    screen.hline(11,2,2,1)
    screen.hline(9,3,2,1)
    screen.hline(13,3,2,1)
    
    screen.show()
    
def neutralOne():
    screen.fill(0)
    
    screen.vline(0,2,4,1)
    screen.vline(7,2,4,1)
    screen.hline(2,0,4,1)
    screen.hline(2,7,4,1)
    screen.pixel(1,1,1)
    screen.pixel(6,6,1)
    screen.pixel(1,6,1)
    screen.pixel(6,1,1)
    
    screen.vline(8,2,4,1)
    screen.vline(15,2,4,1)
    screen.hline(10,0,4,1)
    screen.hline(10,7,4,1)
    screen.pixel(9,1,1)
    screen.pixel(14,6,1)
    screen.pixel(9,6,1)
    screen.pixel(14,1,1)
    
    screen.show()
    
def neutralTwo():
    screen.fill(0)
    
    screen.vline(0,3,3,1)
    screen.vline(7,3,3,1)
    screen.hline(3,1,2,1)
    screen.hline(1,2,2,1)
    screen.hline(5,2,2,1)
    screen.hline(1,6,2,1)
    screen.hline(5,6,2,1)
    screen.hline(3,7,2,1)
    
    screen.vline(8,3,3,1)
    screen.vline(15,3,3,1)
    screen.hline(11,1,2,1)
    screen.hline(9,2,2,1)
    screen.hline(13,2,2,1)
    screen.hline(9,6,2,1)
    screen.hline(13,6,2,1)
    screen.hline(11,7,2,1)
    
    screen.show()
    
def neutralThree():
    screen.fill(0)
    
    screen.pixel(0,4,1)
    screen.pixel(7,4,1)
    screen.hline(3,2,2,1)
    screen.hline(1,3,2,1)
    screen.hline(5,3,2,1)
    screen.hline(1,5,2,1)
    screen.hline(5,5,2,1)
    screen.hline(3,6,2,1)
    
    screen.pixel(8,4,1)
    screen.pixel(15,4,1)
    screen.hline(11,2,2,1)
    screen.hline(9,3,2,1)
    screen.hline(13,3,2,1)
    screen.hline(9,5,2,1)
    screen.hline(13,5,2,1)
    screen.hline(11,6,2,1)
    
    screen.show()
    
def sadOne():
    screen.fill(0)
    
    screen.vline(0,3,2,1)
    screen.vline(7,3,2,1)
    screen.hline(2,6,4,1)
    screen.pixel(1,5,1)
    screen.pixel(6,5,1)
    
    screen.vline(8,3,2,1)
    screen.vline(15,3,2,1)
    screen.hline(10,6,4,1)
    screen.pixel(9,5,1)
    screen.pixel(14,5,1)
    
    screen.show()
    
def sadTwo():
    screen.fill(0)
    
    screen.vline(0,3,2,1)
    screen.vline(7,3,2,1)
    screen.hline(1,5,2,1)
    screen.hline(5,5,2,1)
    screen.hline(3,6,2,1)
    
    screen.vline(8,3,2,1)
    screen.vline(15,3,2,1)
    screen.hline(9,5,2,1)
    screen.hline(13,5,2,1)
    screen.hline(11,6,2,1)
    
    screen.show()
    
def sadThree():
    screen.fill(0)
    
    screen.pixel(0,3,1)
    screen.pixel(7,3,1)
    screen.hline(1,4,2,1)
    screen.hline(5,4,2,1)
    screen.hline(3,5,2,1)
    
    screen.pixel(8,3,1)
    screen.pixel(15,3,1)
    screen.hline(9,4,2,1)
    screen.hline(13,4,2,1)
    screen.hline(11,5,2,1)
    
    screen.show()