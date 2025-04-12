class Number:
    def __init__(self, n):
        self.n = n
    def __floordiv__(self, num):
        return self.n // num.n

n = Number(6)
m = Number(2)

print(n // m)

'''
__add__ --> Addition
__sub__ --> Subtraction
__mul__ --> Multiplication
__truediv__ --> Division
__floordiv__ --> Get Quotient Only

'''