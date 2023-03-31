## Selbst geschriebene Library für RGBLED für Lil'E
## basiert auf dem Beispielcode von Freenove

# Imports
from machine import Pin,PWM
import time

# Initalisierung
pins=[19,18,5]
pwm0=PWM(Pin(pins[0]),10000)
pwm1=PWM(Pin(pins[1]),10000)
pwm2=PWM(Pin(pins[2]),10000)
 
pins_mirror = [33, 12, 32]
pwm0_mirror=PWM(Pin(pins_mirror[0]),10000)
pwm1_mirror=PWM(Pin(pins_mirror[1]),10000)
pwm2_mirror=PWM(Pin(pins_mirror[2]),10000)
i = 1




# Hilfsfunktionen
def setColor(r,g,b):
 pwm0.duty(1023-r)
 pwm1.duty(1023-g)
 pwm2.duty(1023-b)
 pwm0_mirror.duty(1023-r)
 pwm1_mirror.duty(1023-g)
 pwm2_mirror.duty(1023-b)
 
 

# Library    
def setUserViolet():
     red = 0
     blue = 0
     green = 1023
     setColor(red,green,blue)
     print('Set User Violet')

def setUserBlue():
     red = 1023
     blue = 0
     green = 0
     setColor(red,green,blue)
     print('Set User Blue')
    

def setUserGreen():
     red = 0
     blue = 1023
     green = 0
     setColor(red,green,blue)
     print('Set User Green')
    
    
def disableEars():
     red = 1023
     blue = 1023
     green = 1023
     setColor(red,green,blue)
     print('Ears are disable')

#main-Cycle
def testRGBLed():
    try:
     while True:
       print('----  Test - RGB Led')
       i = i + 1
       # Bedienung der RGB-LED: Wert = 0 bedeutet Farbe so stark, wie möglich, 1023 bedeutet Farbe aus
       setUserViolet()   
       time.sleep(5)
       setUserBlue()
       time.sleep(5)
       setUserGreen()
       time.sleep(5)
       disableEars()
       time.sleep(5)
       print('---- Finished Test. Try:', i)
    except:
       pwm0.deinit()
       pwm1.deinit()
       pwm2.deinit()
       pwm0_mirror.deinit()
       pwm1_mirror.deinit()
       pwm2_mirror.deinit()


