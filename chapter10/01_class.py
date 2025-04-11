class Employee:
    language = "py" # This is a class attribute
    age = 18
    country = "INDIA"
    city = "BANUR" 
    salary = 120000
harsh = Employee()  # 'harsh' is an object here
harsh.name = "Harsh" # This is a instance attribute
print(harsh.country, harsh.age, harsh.city)
print("")
rohan = Employee()
rohan.name = "Rohan Verma" # This is a instance attribute
print(rohan.name, rohan.salary, rohan.language)

# here name is instance attribute and salary and language are 
# class attribute as they directly belong to the class
