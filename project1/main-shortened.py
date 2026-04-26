'''
1 for snake
-1 for water
0 for gun

'''
import random
computer = random.randint(-1, 1)

youstr =input("Enter your choice: ")

youDict = {"s": 1, "w": -1, "g": 0}

reverseDict = {1: "snake", -1: "water", 0: "gun"}

you = youDict[youstr]

print(f"you chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")

if(computer == you):
    print("It's a tie")

else:
    '''
    
    if(computer == -1 and you == 1) :
        print("You win")

    elif(computer == -1 and you == 0):
        print("You lose")

    elif(computer == 1 and you == -1):
        print("You lose")

    elif(computer == 1 and you == 0):
        print("You win")

    elif(computer == 0 and you == 1):
        print("You lose")

    elif(computer == 0 and you == -1):
        print("You win")


    else:
        print("something went wrong")
    '''

 ## the below logic is written on the basis of the value of computer - you
if(computer - you == -1 or (computer - you == 2)):
    print("you lose!")

else:
    print("you win !")