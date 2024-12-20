from time import *
from random import *
from microbit import *
from music import *
from radio import *

config(group = 35)

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
            main()


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
            main()


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
            main()


#night light
def nightLight():
    display.clear()

    while True:

        #check if light level is below 50
        if display.read_light_level() < 6:
            display.show(Image('99999:'
                               '99999:'
                               '99999:'
                               '99999:'
                               '99999'))

        else: 
            display.clear()

        #if B was pressed, exit to menu
        if button_b.was_pressed():
            display.clear()
            main()


#rock paper scissors
def rps():
    display.clear()
    display.scroll('RPS')

    while True:
        #when shake, play
        if accelerometer.was_gesture('shake'):
            rpsDes = randint(1, 3)

            #rock
            if rpsDes == 1:
                display.show(Image('00000:'
                                   '09990:'
                                   '09090:'
                                   '09990:'
                                   '00000'))

            #paper
            elif rpsDes == 2:
                display.show(Image('99999:'
                                   '90009:'
                                   '90009:'
                                   '90009:'
                                   '99999'))

            #scissors
            else:
                display.show(Image('99009:'
                                   '99090:'
                                   '00900:'
                                   '99090:'
                                   '99009'))

        #if B was pressed, exit to menu
        if button_b.was_pressed():
            display.clear()
            main()

#radio test
def radio():
    display.clear()
    on()

    while True:

        #message reciving stuff
        message = receive()

        if message:
            display.scroll(message)

        #if A was pressed, send "aloo"
        if button_a.was_pressed():
            send('aloo')
            display.scroll('sent')
            

        #if B was pressed, exit to menu
        if button_b.was_pressed():
            display.clear()
            off()
            main()

#temperature
def temp():
    display.clear()

    display.show('T')
    
    while True:
        
        #display temp
        if button_a.was_pressed():
            display.scroll(temperature())

        #if B was pressed, exit to menu
        if button_b.was_pressed():
            display.clear()
            main()

########  vvvvv TEST THIS ON FRIDAY vvvvv ########

#compass
def comp():
    display.clear()
    compass.calibrate()

    while True:

        #show direction
        if button_a.was_pressed():
            display.show(compass.heading())

        #if B was pressed, exit to menu
        if button_b.was_pressed():
            display.clear()
            main()


#main script picker code
def main():
    desX = 0
    desY = 0

    while True:

        #lights up the pixel currently being targeted
        display.set_pixel(desX, desY, 9)

        if button_b.was_pressed():

            #if it is right by the right side, make it loop back to the left 
            #and clear the other pixels
            if desX == 4:
                desX = 0

                #if at bottom, scroll back to top
                if desY == 4:
                    display.clear()
                    desY = 0

                else:
                    desY += 1

            #move the pixel 1 to the right
            else: 
                desX += 1

        #picking the function using above script:
    
        if button_a.was_pressed():
        
            #heart function
            if desX == 0 and desY == 0:
                heart()

            #dice function
            elif desX == 1 and desY == 0:
                dice()

            #steptracker function
            elif desX == 2 and desY == 0:
                steptracker()

            #night light
            elif desX == 3 and desY == 0:
                nightLight()

            #rock paper scissors
            elif desX == 4 and desY == 0:
                rps()

            #radio
            elif desX == 0 and desY == 1:
                radio()
            
            #temperature
            elif desX == 1 and desY == 1:
                temp()
            
            #compass
            elif desX == 2 and desY == 1:
                #comp()
                pass
            
            #empty space
            elif desX == 3 and desY == 1:
                pass
            
            #empty space
            elif desX == 4 and desY == 1:
                pass
            
            #empty space
            elif desX == 0 and desY == 2:
                pass
            
            #empty space
            elif desX == 1 and desY == 2:
                pass
            
            #empty space
            elif desX == 2 and desY == 2:
                pass
            
            #empty space
            elif desX == 3 and desY == 2:
                pass
            
            #empty space
            elif desX == 4 and desY == 2:
                pass
            
            #empty space
            elif desX == 0 and desY == 3:
                pass
            
            #empty space
            elif desX == 1 and desY == 3:
                pass
            
            #empty space
            elif desX == 2 and desY == 3:
                pass
            
            #empty space
            elif desX == 3 and desY == 3:
                pass
            
            #empty space
            elif desX == 4 and desY == 3:
                pass
            
            #empty space
            elif desX == 0 and desY == 4:
                pass
            
            #empty space
            elif desX == 1 and desY == 4:
                pass
            
            #empty space
            elif desX == 2 and desY == 4:
                pass
            
            #empty space
            elif desX == 3 and desY == 4:
                pass
            
            #empty space
            elif desX == 4 and desY == 4:
                pass

main()