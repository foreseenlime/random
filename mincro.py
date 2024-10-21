from time import *
from random import *
from microbit import *
from music import *

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
            display.clear()
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

#main script picker code
def main():
    des = 0

    while True:

        #lights up the pixel currently being targeted
        display.set_pixel(des, 2, 9)

        if button_b.was_pressed():

            #if it is right by the right side, make it loop back to the left 
            #and clear the other pixels
            if des == 4:
                display.clear()
                des = 0

            #move the pixel 1 to the right
            else: 
                des += 1

        #picking the function using above script:
    
        if button_a.was_pressed():
        
            #heart function
            if des == 0:
                heart()

            #dice function
            elif des == 1:
                dice()

            #steptracker function
            elif des == 2:
                steptracker()

            #empty space
            elif des == 3:
                pass

            #empty space
            elif des == 4:
                pass


main()

#               IDEAS:                  #

# -instead of the while True, make a function for the main script that 
#  can be run when you want to end a function but break doesnt work