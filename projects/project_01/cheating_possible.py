import random
computer = random.choice([1, 0, -1])
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

print(f"Computer Chose: {reverseDict[computer]}")
youStr = input("(w: water, g: gun, s: snake)\nEnter Your choice(w/g/s): ").lower()
you = youDict[youStr]

# By now we have 2 numbers(variables), you and computer
print("")
print(f"You Chose: {reverseDict[you]}\nComputer Chose: {reverseDict[computer]}")
# print() mentioned above shows the option chose randomly by computer and by you
# we used reverseDict in print() because it took input as number and numbers were well defined in this Dictionart

# ------------------------IF LADDER BELOW ------------------------
if(computer == you):
    print("It's a Draw")
else:
    if((computer - you) == -1 or (computer - you) == 2 ):
        print("YOU LOOSE!\nBETTER LUCK NEXT TIME!")
    else:
        print("YOU WIN!\nWELL PLAYED!")

print("THANKS FOR PLAYING!😊")
