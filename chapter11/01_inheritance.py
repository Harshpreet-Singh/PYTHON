class Employee:    # THIS IS PARENT/BASE CLASS
    company = "ITC"
    def show(self):
        print(f"The name is {self.name} & The salary is {self.salary}")

# class Programmer:
#     company = "ITC Infotch"
#     def show(self):
#         print(f"The name is {self.name} & The salary is {self.salary}") 

#     def showLanguage(self):
#         print(f"The name is {self.name} & He is good with {self.language} language")

# ^^^^^^^^^^^^^^^^^^^^^^ _USE THE FOLLOWING METHOD INSTEAD OF THE ABOVE ONE_ ^^^^^^^^^^^^^^^^^^^^^^^^^

class Programmer(Employee):   # THIS IS INHERITED CLASS 
    company = "ITC InfoTech"
    def showLanguage(self):
        print(f"The name is {self.name} & He is good with {self.language} language")

a = Employee()
b = Programmer()
a.name = "Rohan"
print(a.company, b.company, a.name)