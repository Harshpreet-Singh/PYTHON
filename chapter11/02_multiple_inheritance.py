# MULTIPLE INHERITANCE MEANS FROM 2 PARENTS/BASE CLASSES WE MAKE 1 CHILD CLASS

class Employee: #/\/\/\/\/\/\/\__PARENTS/BASE CLASS__/\/\/\/\/\/\/\
    # company = "ITC"
    # name = "Default Name"
    # salary = 120000
    name = input("Enter Your Name: ")
    company = input("Enter Your Company you work with: ")
    salary = int(input("Enter Your Salary Here: "))
    def show(self):
        print(f"The name is {self.name} & The salary is {self.salary}")

class Coder: #/\/\/\/\/\/\/\__PARENTS/BASE CLASS__/\/\/\/\/\/\/\
    # language = "Python"
    language = input("Enter the language you are good with: ")
    def printLanguages(self):
        print(f"Here is your Language: {self.language}")

class Programmer(Employee, Coder): #/\/\/\/\/\/\/\__CHILD CLASS__/\/\/\/\/\/\/\
    company = "ITC InfoTech" # COMAPNY IS DEFINED HERE AGAIN SO THIS VALUE WILL GET PRIORITY
    def showLanguage(self):
        print(f"He work with {self.company} & He is good with {self.language} language")

#    CALLING CLASSES
a = Employee()
b = Programmer()

#   CALLING FUNCTIONS HERE
b.show()
b.printLanguages()
b.showLanguage()