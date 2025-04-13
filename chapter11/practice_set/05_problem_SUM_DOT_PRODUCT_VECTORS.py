class ThreeDVector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")
    def dot(self):
        print(f"The dot product of above 2 vector is: {ii_1*ii_2}i + {jj_1*jj_2}j + {kk_1*kk_2}k")
    def sum(self):
        print(f"The sum of above 2 vector is: {ii_1+ii_2}i + {jj_1+jj_2}j + {kk_1+kk_2}k")

print("Mention the first vector below-->")
ii_1 = int(input("Enter value of i: "))
jj_1 = int(input("Enter value of j: "))
kk_1 = int(input("Enter value of k: "))

print("Mention the second vector below-->")
ii_2 = int(input("Enter value of i: "))
jj_2 = int(input("Enter value of j: "))
kk_2 = int(input("Enter value of k: "))

a = ThreeDVector(ii_1, jj_1, kk_1)
b = ThreeDVector(ii_2, jj_2, kk_2)
a.show()
b.show()
a.dot()
a.sum()