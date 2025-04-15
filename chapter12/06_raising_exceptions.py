a = int(input("Hey! Enter first Number: "))
b = int(input("Hey! Enter second Number: "))
# div = int(a/b)  # making it integar removes its decimals
if(b == 0):
    raise ZeroDivisionError("\033[1;91mHey! Your division is not meant to divide number by zero\033[0m")
else:
    div = round(a/b, 2)  # making it decimal with 2 after decimal values
    print(f"The division of {a}/{b} is {div}")
