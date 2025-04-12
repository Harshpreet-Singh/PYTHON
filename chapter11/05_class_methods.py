class Employee():
    a = 1
    @classmethod     # a = 1 will be prioritized now
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = Employee()
e.a = 45  # instance attribute
e.show() 