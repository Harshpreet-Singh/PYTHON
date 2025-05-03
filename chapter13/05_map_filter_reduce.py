# MAP EXAMPLE
from functools import reduce


l = [1, 2, 3, 4, 5, 6]
square = lambda x: x*x

sqList = map(square, l)
print(list(sqList))

# FILTER EXAMPLE

def even(n):
    if(n%2 == 0):
        return True
    return False   # no need to write else here
onlyEven = filter(even, l)
print(list(onlyEven))

# REDUCE EXAMPLE
def sum(a, b):
    return a+b

print(reduce(sum, l))
# this is a type of submission
# this will sum first two and consider it as one number than consider that one and next number and so on..
mul = lambda x,y: x*y
print(reduce(mul, l))  
# this is a type of factorial