'''
1 for Snake
-1 for Water
0 for Gun
'''

import random

# number = random.choice([1, 0, -1])
# print(number)


computer = random.choice([1, 0, -1])
youStr = input("Enter Your choice: ")
youDict = {
    "s": 1,
    "w": -1,
    "g": 0
}
reverseDict = {
    1 : "Snake",
    -1: "Water",
    0: "Gun"
}
you = youDict[youStr]

# By now we have 2 numbers(variables), you and computer

print(f"You Chose: {reverseDict[you]}\nComputer Chose: {reverseDict[computer]}")

# print() mentioned above shows the option chose randomly by computer and by you
# we used reverseDict in print() because it took input as number and numbers were well defined in this Dictionart


# IF LADDER BELOW 
if(computer == you):
    print("It's a Draw")
else:
    if((computer - you) == -1 or (computer - you) == 2 ):
        print("YOU LOOSE!\nBETTER LUCK NEXT TIME!")
    else:
        print("YOU WIN!\nWELL PLAYED!")
# THIS LOGIC IS WRITTEN ON LOGIN MENTIONED BELOW:
# COMPUTER-YOU ki jo value hai use check kiya gya
# it was -1 or 2 if player loose so we added condition on (computer-you)'s value          
print("Thanks for playing!")
