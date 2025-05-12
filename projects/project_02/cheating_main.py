from random import randint
n = randint(1, 100)
print(f"The Number is : {n}")
a=-1
guesses = 0
while(a != n):
    a = int(input("Guess the Number: "))
    if(a == n):
        print("You won!\nWell Played")
        print(f"Yeah, The Number was {n}")
        print(f"You guessed the number in {guesses} times")
        break
    elif(a > n):
        print(f"Guess a lower number than {a}")
    elif(a < n):
        print(f"Guess a greater number than {a}")
    elif(a < 0):
        print(f"The number is positive")
    else:
        print("Opps, Something Went Wrong!")