# THE FACTORIAL OF THE NUMBER YOU ENTERED
n = int(input("Enter a Number: "))
product = 1
for i in range(1, n+1):
    product = product*i

print(f"The factorial of {n} is {product}")