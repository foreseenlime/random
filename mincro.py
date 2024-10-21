from time import *
from random import *
from microbit import *
from music import *


display.show(Image.HAPPY)


#heart beating function
def heart():
    while True:

        #repeats 2 time:
        #small heart, big heart, small heart

        for i in range(2):
            display.show(Image.HEART_SMALL)
            sleep(150)
            display.show(Image.HEART)
            sleep(150)
            display.show(Image.HEART_SMALL)
        
        #wait in between each 2 heart beats
        sleep(400)

        #checks if button was pressed to see if it needs to be cancelled
        if button_b.was_pressed():
            display.clear()
            break


#dice function
def dice():
    display.show(Image.ANGRY)
    while True:

        #if microbit was shaken, display random number
        if accelerometer.was_gesture('shake'):
            play(BA_DING)
            display.show(randint(1, 6))
        
        #checks if button was pressed to see if it needs to be cancelled
        if button_b.was_pressed():
            break


#steptracker function
def steptracker():

    #clear display and reset step count
    display.clear()
    steps = 0
    while True:

        #if microbit was shaken (step taken) increase step count and display it
        if accelerometer.was_gesture('shake'):
            steps += 2
            display.show(steps)

        #check if button was pressed to see if it needs to be cancelled
        if button_b.was_pressed():
            display.clear()
            break

while True:
    if button_a.is_pressed():
        dice()

    if button_b.is_pressed():
        pass

    if pin_logo.is_touched():
        pass





#               IDEAS:                  #

# -instead of the while True, make a function for the main script that can be run when you want to end a 
#  function but break doesnt work

# - make a function picker similar to what you had at the start, where pressing B changed a pixel on the display, 
#   and pressing A picks the function