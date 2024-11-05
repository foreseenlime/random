from microbit import *
from time import *
from random import *

playerP = 2
exPlayerP = 2

bulletP = 3
exBulletP = 3

display.set_pixel(2, 4, 9)

while True:

    if button_a.is_pressed():
        if playerP != 0:
            playerP -= 1
            display.set_pixel(playerP, 4, 9)
            display.set_pixel(exPlayerP, 4, 0)
            exPlayerP = playerP
            sleep_ms(100)

    if button_b.is_pressed():
        if playerP != 4:
            playerP += 1
            display.set_pixel(playerP, 4, 9)
            display.set_pixel(exPlayerP, 4, 0)
            exPlayerP = playerP
            sleep_ms(100)

    if button_a.is_pressed() and button_b.is_pressed():
        display.set_pixel(playerP, bulletP, 9)

    if pin_logo.is_touched():
        pass