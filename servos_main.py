from servo import Servo
import time

# ear2 is right side
# ear1 is left side
motor=Servo(pin=27)
ear1=Servo(pin=25)
ear2=Servo(pin=26)

def move_arm_up():
    print(motor.current_angle)
    motor.move(0)
    print(motor.current_angle)
    motor.move(120)
    print(motor.current_angle)
    



def move_arm_down():
    print(motor.current_angle)
    motor.move(120)
    print(motor.current_angle)
    motor.move(0)
    print(motor.current_angle)
    


def ears_default():
    ear1.move(0)
    ear2.move(140)
    ear1.move(140)
    ear2.move(0)


def ears_half_back():
    ear1.move(140)
    ear2.move(0)
    ear1.move(90)
    ear2.move(45)


def ears_back():
    ear1.move(90)
    ear2.move(45)
    ear1.move(45)
    ear2.move(90)


def ears_down():
    ear1.move(90)
    ear2.move(90)
    ear1.move(0)
    ear2.move(140)

#move_arm_up()
#move_arm_down()
#ears_default()
#ears_half_back()
#ears_back()
#ears_down()



