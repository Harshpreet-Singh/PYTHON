# cm=inches×2.54
def convert(n):
    return n * 2.54

n = int(input("Enter Centimeters: "))
a = round(convert(n), 2)
print(f"{n} cms in inches = {a}")
#or
print(f"{n} cms in inches = {convert(n)}")