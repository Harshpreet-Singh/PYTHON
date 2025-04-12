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
print("\n bellow is use of __str__ & __repr__")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."
    
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

p = Person("Harshpreet", 23)
print(p) # Uses __str__
print(str(p)) # Also uses __str__
print(repr(p))   # Uses __repr__

people = [Person("Harsh", 25), Person("Simran", 28)]
print(people)
