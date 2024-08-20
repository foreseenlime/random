import random 
import tkinter as tk


#                      WINDOW
def window():
    win = tk.Tk()
    ss = tk.PhotoImage(file = "screenShot.png")
   # count = 0

   # def click():
   #     global count
   #     count += 1
   #     print(count)

   # button = tk.Button(win, text = "Click")
    
   # button.config(command = click, )
   # button.config(font = ("Arial", 40, "bold"))
   # button.config(bg = "black")
   # button.config(fg = "green")
   # button.config(activebackground = "black")
   # button.config(activeforeground = "green")
    
    label = tk.Label(
        text = "yippies",
        font = ("Arial", 30, "bold"),
        fg = "black",
        bg = "white",
        pady = 20,
        padx = 20,
        compound = "bottom"
    )

   # button.pack()
    label.pack()
    win.mainloop()





#                     CALCULATOR
def calculator():
    playerNumberOne = int(input("first number: "))
    playerNumberTwo = int(input("second number: "))
    playerEquation = input("equation: ")

    #player requests addition
    if "+" or "plus" in playerEquation:
        ans = playerNumberOne + playerNumberTwo
        print("---------")
        print(ans)
        print("---------")

    #player requests subtration
    elif "-" or "minus" in playerEquation:
        ans = playerNumberOne - playerNumberTwo
        print("---------")
        print(ans)
        print("---------")
    #player requests multiplication
    elif "*" or "times" in playerEquation:
        ans = playerNumberOne * playerNumberTwo
        print("---------")
        print(ans)
        print("---------")

    #player requests division
    elif "/" or "divided" in playerEquation:
        ans = playerNumberOne / playerNumberTwo
        print("---------")
        print(ans)
        print("---------")

    elif "2900":
        print("bhzdkbndzcxj,dnzkxnjk")

    else:
        print("please try again later")





#                           ROCK PAPER SCISSORS 
def rockPaperScissors():
    com = random.randint(1, 3)
    repeatNum = 1

    #loop so you can replay
    while repeatNum == 1:
        print("lets play rock paper scissors!")

        playerInput = int(input("type 1, 2, or 3, for rock, paper, or scissors: "))

        #Player chooses rock:
        if playerInput == 1:
            playerDesicion = "rock"
    
            if com == 1:
                print("--------------------------------")
                print('com picked rock! you tied!')
                print("--------------------------------")
    
            elif com == 2:
                print("--------------------------------")
                print('com picked paper! you lose :(')
                print("--------------------------------")

            else:
                print("--------------------------------")
                print('com picked scissors! you win! :D')
                print("--------------------------------")

        #Player chooses paper:
        elif playerInput == 2:
            playerDesicion = "paper"

            if com == 1:
                print("--------------------------------")
                print("com chose rock! you win! :D")
                print("--------------------------------")

            elif com == 2:
                print("--------------------------------")
                print("com chose paper! you tie!")
                print("--------------------------------")

            else:
                print("--------------------------------")
                print("com chose scissors! you lose :(")
                print("--------------------------------")

        #Player chooses scissors:
        elif playerInput == 3:
            playerDesicion = "scissors"

            if com == 1:
                print("--------------------------------")
                print("com chose rock! you lose :(")
                print("--------------------------------")

            elif com == 2:
                print("--------------------------------")
                print("com chose paper! you win :D")
                print("--------------------------------")

            else:
                print("--------------------------------")
                print("com chose scissors! you tie!")
                print("--------------------------------")

        elif playerInput == 35:
            print("----------")
            print("pizza cake")
            print("----------")

        elif playerInput == 27:
            print("--------------------------------------------------------------------------------")
            print("omg you are so cool if you see this it means you win even when it says u lose :D")
            print("--------------------------------------------------------------------------------")

        else:
            print("that wasn't one of the options. you lose by default")

    #this is for if the player wants to play again
        replayDesicion = input("play again (y/n) ")

        if replayDesicion == "y":
            com = random.randint(1, 3)
            print("-------------------------------------")
            continue

        elif replayDesicion == "n":
            break

        else:
            break


print("------------------------------------------")
print("Welcome! please choose what you want to do")
choice = input()
print("------------------------------------------")

if choice == "window" or choice == "win":
    window()

elif choice == "calculator" or choice == "cal":
    calculator()

elif choice == "rps":
    rockPaperScissors()

else:
    print("sorry, that didnt work")