a = input("Enter number 1: ")

# b = input("Enter number 2: ")

c = int(a)
# d = int(b)
d = int(input("Enter number 2: "))
# if we don't use this converter here then it will show '5+7= 57'
# this is becuase here a was initially defined as a string but later converted to integer
print("  ")
print("Number a is: ", c)
print("  ")
print("Number b is: ", d)
print("  ")
print("Sum is: ", c * d)
