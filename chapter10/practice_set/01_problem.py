class Programmmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

    def __str__(self):
        return f"{self.name}, {self.company}, {self.salary}, {self.pin}\n"

nam = input("Enter Your Name Here: ")
slr = int(input("Enter Your Salary Here: "))
pincode = (input("Enter Your Pincode: "))
p = Programmmer(nam, slr, pincode)
if(len(pincode)<6):
    print("Enter a Valid pincode of 6 digits!")
else:
    # p = Programmer(nam, slr, pincode)
    print(p.name, p.company, p.salary, p.pin)
    with open("chapter10\\practice_set\\01_data.txt", "a") as f:
        f.write(str(p))
        print("Done!")