from microbit import *
from time import *
from random import *

playerP = 2
exPlayerP = 2

bulletP = 4
exBulletP = 3

display.set_pixel(2, 4, 9)

def moveLeft():
    global playerP
    global exPlayerP
    if playerP != 0:
            playerP -= 1
            display.set_pixel(playerP, 4, 9)
            display.set_pixel(exPlayerP, 4, 0)
            exPlayerP = playerP
            while True:
                if button_a.is_pressed() == False:
                    break

def moveRight():
    global playerP
    global exPlayerP
    if playerP != 4:
            playerP += 1
            display.set_pixel(playerP, 4, 9)
            display.set_pixel(exPlayerP, 4, 0)
            exPlayerP = playerP
            while True:
                if button_b.is_pressed() == False:
                    break

def shoot():
    global bulletP
    global exBulletP
    global playerP
    bulletP -= 1
    display.set_pixel(playerP, bulletP, 9)
    sleep_ms(100)
    x = playerP
    while bulletP != 0:
        bulletP -= 1
        display.set_pixel(x, bulletP, 9)
        display.set_pixel(x, exBulletP, 0)
        exBulletP = bulletP
        sleep_ms(100)

    display.set_pixel(x, exBulletP, 0)

    bulletP = 4
    exBulletP = 3
    while True:
        if pin_logo.is_touched() == False:
            break
    

while True:

    if button_a.is_pressed():
        moveLeft()

    if button_b.is_pressed():
        moveRight()

    if pin_logo.is_touched():
        shoot()


