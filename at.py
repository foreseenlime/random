from microbit import *
from time import *
from random import *

playerP = 2
exPlayerP = 2

bulletP = 2
exBulletP = 2

display.set_pixel(2, 4, 9)

while True:

    if button_a.was_pressed():
        if playerP != 0:
            playerP -= 1
            display.set_pixel(playerP, 4, 9)
            display.set_pixel(exPlayerP, 4, 0)
            exPlayerP = playerP

    if button_b.was_pressed():
        if playerP != 4:
            playerP += 1
            display.set_pixel(playerP, 4, 9)
            display.set_pixel(exPlayerP, 4, 0)
            exPlayerP = playerP

    if pin_logo.is_touched():
        for i in range(4):
            pass