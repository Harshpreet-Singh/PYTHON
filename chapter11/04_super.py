class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1

class Programmer(Employee): 
    def __init__(self):
        super().__init__()
        print("Constructor of Programmer")
    b = 2

class Manager(Programmer): 
    def __init__(self):
        super().__init__() #    THIS IS USED TO CALL ITS PARENT CLASS
        print("Constructor of Manager")
    c = 3

        
#    CREATING OBJECT
# o = Employee()
# print(o.a)
# o = Programmer()
# print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c)