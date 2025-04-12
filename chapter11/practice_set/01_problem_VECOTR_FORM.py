class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")

class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")

ii = int(input("Enter value of i: "))
jj = int(input("Enter value of j: "))
kk = int(input("Enter value of k: "))

# a = TwoDVector(2, 9)
# b = ThreeDVector(2, 9, 8)

a = TwoDVector(ii, jj)
b = ThreeDVector(ii, jj, kk)
a.show()
b.show()