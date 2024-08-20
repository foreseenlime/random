playerNumberOne = 0
playerNumberTwo = 0
playerEquation = 0
ans = 0

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