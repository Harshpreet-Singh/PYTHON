import os
import time
from random import randint

pas = input("Tell the Password (4 digits only): ")

keys = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        'a','b','c','d','e','f','g','h','i','j','k','l','m',
        'n','o','p','q','r','s','t','u','v','w','x','y','z']

pwg = ""

start_time = time.time()  # ⏱️ Start the timer

while pwg != pas:
    pwg = ""
    for i in range(len(pas)):
        guessPass = keys[randint(0, 4)]
        pwg = str(guessPass) + str(pwg)
    print(pwg)
    print("Attacking... Please wait")
    os.system("cls")

end_time = time.time()  # ⏱️ End the timer

time_taken = end_time - start_time

print(f"The Passcode is: {pwg}")
print(f"Time taken to crack: {time_taken:.2f} seconds")
