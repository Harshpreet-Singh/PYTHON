a = 89 # here a is a global variable that can be used inside or outside the function
def fun():
    global a # now a outside fn will be considered and changed inside funciton
    a = 3  # here a is a local variable that can be only used inside the funciton
    print(a)
fun()
print(a)