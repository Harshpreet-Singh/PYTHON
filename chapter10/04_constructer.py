class Employee:
    language = "Python" # This is a class attribute
    age = 18
    country = "INDIA"
    city = "BANUR" 
    salary = 120000

    def __init__(self, name, salary, language):  # this is dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")
harsh = Employee("Harsh", 130000, "PHP")    # define attributes like this [THEY GET PRIORITY]

print(f"My name is {harsh.name}\nI love {harsh.language}\nMy salary is: {harsh.salary}\nMy age is: {harsh.age}\nI live in {harsh.city}")
