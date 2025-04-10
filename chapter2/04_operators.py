# arithmetic operators

from tkinter import E


a = 34 
b = 4
c = a+b
print(c)

# assignment operators
P = 4-2 # assign 4-2 in a 
Q = 6
Q += 3  # inrement the value of b by 3 and then assign it to Q
# Q -= 3  # decrement the value of b by 3 and then assign it to Q
# Q *= 3  # multiply the value of b by 3 and then assign it to Q
# Q /= 3  # divide the value of b by 3 and then assign it to Q
print(P)
print(Q)

# Comparison operators

d = 3<=5 # less than equal to is defined like this
e = 3>5 # greater than is defined like this 
f = 1==1 # equal is defined with double ==, as single is used to define variable
g = 1!=1 # 1 not equal to one
print(d)
print(e)
print(f'f is, {f}')
print("g is ", g)


# logical operators

# in {or} true gets the priority
# in {and} false gets the priority

i = True or False
j = True or True
print("True or False is ", i)
print("True or True is ", j)
# print("False or True is ", False or True)
# print("False or False is ", False or False)
print("  ")
k = True and False
print("True and False is ", k) # agar false hai ek bhi condition so false hi hai


# not operators
# This gives you the opposite of True/False
l = False
print(not(l))