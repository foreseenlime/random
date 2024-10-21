from time import *
from random import *
from microbit import *
from music import *
display.show(Image.HAPPY)

def heart():
    while True:

        for i in range(2):
            display.show(Image.HEART_SMALL)
            sleep(150)
            display.show(Image.HEART)
            sleep(150)
            display.show(Image.HEART_SMALL)
        
        
        sleep(400)

        if button_b.was_pressed() and button_a.was_pressed:
            display.clear()
            break

def dice():
    display.show(Image.ANGRY)
    while True:

        if accelerometer.was_gesture('shake'):
            play(BA_DING)
            display.show(randint(1, 6))

        # add an IF command that checks if it was shaken
        # when it is shaken make it display a random number
        
        if button_a.was_pressed() and button_b.was_pressed():
            break

def steptracker():
    display.clear()
    steps = 0
    while True:

        if accelerometer.was_gesture('shake'):
            steps += 2
            display.show(steps)

        if button_a.was_pressed():
            display.clear()
            break

while True:
    if button_a.is_pressed():
        dice()

    if button_b.is_pressed():
        pass

    if pin_logo.is_touched():
        pass