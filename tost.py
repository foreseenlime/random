import random as ran
import tkinter as tk

a = 0
b = ran.randint(1, 3)
c = 69

def dice():
    for i in range(ran.randint(1, 6)):
        print(i)

while True:
    a = input("sdnjflk jdfkl: ")
    if a == "hello":
        dice()