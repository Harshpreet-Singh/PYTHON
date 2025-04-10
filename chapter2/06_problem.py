# steps are as follows to find the remainder 
# define a variable
# make it integer
# print the varible
a = int(input("Enter Number 1: " ))
b = int(input("Enter Number 2: " ))
# ///////////////////////////////////////////////////////////////////////
# Example of floor division
# quotient_floor = a // b
# print("Quotient (floor division):", quotient_floor)
print("Quotient when", a, end=" ") 
print("is divided by", b, end=" ")  
print("is :", a // b)
#  { , end=" " } use this to continue different prints in same line
print("Remainder when", a, end=" ") 
print("is divided by", b, end=" ")  
print("is :", a % b)
# print("Remainder when a is divided by b is :", a % b)
#  ////////////////////////////////////////////////////////////////////////
# using comparison operator here
t = a>b
print(t, end=" ")
print(a,", is greater than", end=" ")
print(b)
# /////////////////////////////////////////////////////////////////////////

