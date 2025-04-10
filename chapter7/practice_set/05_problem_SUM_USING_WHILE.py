# THE NATURAL NUMBERS TILL THE NUMBER YOU ENTER WILL BE ADDED UP
n = int(input("Enter a Number: "))

i = 1
sum = 0
while(i<=n):
    sum += i
    i += 1

print(sum)