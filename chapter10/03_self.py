class Employee:
    language = "py" # This is a class attribute
    age = 18
    country = "INDIA"
    city = "BANUR" 
    salary = 120000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    @staticmethod
    def greet(): # writing self is important here
        print(f"Thankss..{harsh.name}")
harsh = Employee()
harsh.name = "Harshpreet"
harsh.language = "javascript" # This is a instance attribute {PRIORITY}
print(harsh.language, harsh.salary, harsh.age, harsh.city)
print("")
harsh.getInfo()  # or write it as Employee.getInfo(harsh)
harsh.greet()  # WITHOUT THIS YOU CAN'T PRINT, THIS IS CALLING A FUNCION
