# MULTILEVEL INHERITANCE MEANS FROM 1 PARENTS/BASE CLASSES 
# WE MAKE 1 CHILD CLASS
# AND FROM CHILD_1 CLASS WE MAKE CHILD_2 CLASS

class Employee: #/\/\/\/\/\/\/\__PARENTS/BASE CLASS__/\/\/\/\/\/\/\
    a = 1

class Programmer(Employee): #/\/\/\/\/\/\/\__CHILD_2 CLASS__/\/\/\/\/\/\/\
    b = 2

class Manager(Programmer): #/\/\/\/\/\/\/\__CHILD_1 CLASS__/\/\/\/\/\/\/\
    c = 3

        
#    CREATING OBJECT
o = Employee()
print(o.a)
# print(o.b)  PRINT ERROR AS THERE IS NO 'b' IN Employee()
m = Manager
print(m.a, m.b, m.c)