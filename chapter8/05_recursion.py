def factorial(n):
    if(n == 1 or n == 0):
        return 1
    elif(n<0):
        return "Not Possible\nPlease Enter a Valid & Positive Number"
    return n * factorial(n-1)


n = int(input("Enter a Number: "))
print(f"The Factorial of {n} is: {factorial(n)}")