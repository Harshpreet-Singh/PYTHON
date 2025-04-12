class Employee:
    salary = 234
    increment = 20
    @property   # USING THIS WE CAN RETURN ANYTHING
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
         self.increment = ((salary/self.salary) - 1)*100
         # SALARY = NEW SALARY
         # SELF.SALARY = OLD SALARY
    
e = Employee()
# print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 280.8
print(e.increment)