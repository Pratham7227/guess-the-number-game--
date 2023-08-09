

# Number Guessing Game

import random

randomNumberByComputer=random.randrange(1,20) 

print("Welcome to Number Guessing Game :)")
print("Computer is already generated the number")
userChance=0
while(userChance != randomNumberByComputer):
    numberGuessByUser=int(input("Please Guess the number between 1 To 20:"))
    if(numberGuessByUser==randomNumberByComputer):
        break
    print("Sorry your Guess is Wrong please try again :(")
    userChance+=1

print(f"You takes {userChance} number of times to Guess the number!")    






