import random as ran
import tkinter as tk

a = 0
b = ran.randint(1, 3)
c = 69

str = input("Secret phrase? ")

let1 = str[0]
let2 = str[1]
let3 = str[- 2]
let4 = str[- 1]

print(f"The treasure is in the {let1}{let2}{let3}{let4}!")