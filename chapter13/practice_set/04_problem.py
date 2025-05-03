
from functools import reduce


a = [1,2,15,10,52,48,45,89,70,78,51,41,40,111,152,325]
def greater(a,b):
    if(a>b):
        return a
    return b

print("The Greatest Number is: ", end="")
print(reduce(greater, a))