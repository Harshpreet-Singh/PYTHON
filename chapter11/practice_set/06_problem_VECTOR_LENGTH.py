class Vector:
    def __init__(self,  l):
        self.l = l

    # def __add_(self, other):
    #     result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    #     return result

    # def __null__(self, other):
    #     result = self.x * other.x, self.y * other.y, self.z * other.z
    #     return result

    # def __str__(self):
    #     return f"Vector({self.x}, {self.y}, {self.z})"

    def __len__(self):
        return len(self.l)


# Test the implementation
v1 = Vector([1, 2, 3])
print(len(v1))