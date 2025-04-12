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

print("\n \n bellow is use of __len__")

class Team:
    def __init__(self, members):
        self.members = members
# print(len(t))  # ❌ This will raise: TypeError: object of type 'Team' has no len()

    def __len__(self):
        return len(self.members)

t = Team(["Harsh", "Simran", "Raj"])
print(f"Length of Your Team is: {len(t)}")  # ✅ Output: 3