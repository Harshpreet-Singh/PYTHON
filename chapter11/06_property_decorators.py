class Employee():
    a = 11

    @classmethod     # a = 1 will be prioritized now
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self, value):
        parts = value.split(" ")
        self.fname = parts[0]
        self.lname = parts[1] if len(parts) > 1 else  '' # this leaves line
        self.llname = parts[2] if len(parts) > 2 else  ''
#           'IF & ELSE' IS USED HERE SO THAT IF LAST-LAST NAME DOES NOT EXISTS
#           IT SHOULD NOT GIVE ERROR 


e = Employee()
e.a = 45  # instance attribute

e.name = "Harshpreet Singh"
print(e.fname)  # THIS PRINTS FIRST NAME
print(e.lname)  # THIS PRINTS LAST NAME
print(e.llname)  # THIS PRINTS LAST-LAST NAME
print(e.name)   # THIS PRINTS FULL NAME not the last-last name because in line 9 it is not mentioned


e.show()  



