def change(f):
    c = 5*(f-32)/9
    return c

f = int(input("Enter Temperature in F: "))
change = change(f)
a = round(change, 2)  # this means round change(f) to 2 decimals
print(f"The Value of {f}\u00b0F in Celsius is {a}\u00b0C") 