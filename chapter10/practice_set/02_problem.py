num = int(input("Enter Number Here: "))
class Calculator:
    def __init__(self, n):
        self.n = n
    def square(self):
        print(f"The Square of {self.n} is: {self.n*self.n}") 
    def cube(self):
        print(f"The Cube of {self.n} is: {self.n*self.n*self.n}") 
    def squareRoot(self):
        print(f"The Square Root of {self.n} is: {self.n ** 0.5}")  # {**} double stars means power of number
    @staticmethod
    def greet():
        print("Hello !!")

a = Calculator(num)
a.greet()
a.square()
a.cube()
a.squareRoot()
