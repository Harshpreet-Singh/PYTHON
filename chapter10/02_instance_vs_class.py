class Employee:
    language = "py" # This is a class attribute
    age = 18
    country = "INDIA"
    city = "BANUR" 
    salary = 120000

harsh = Employee()  # 'harsh' is an object here
harsh.language = "javascript" # This is a instance attribute {PRIORITY}
print(harsh.language, harsh.salary, harsh.age, harsh.city)
print("")


# here name is instance attribute and salary and language are 
# class attribute as they directly belong to the class
