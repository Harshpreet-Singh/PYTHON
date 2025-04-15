
try:
    a = int(input("Hey! Enter a Number: "))
    print(a)
except ValueError as v:
    print("Hey!")
    print(v)

except Exception as e:
    print(e) # this protects program from crashing, and prints 'invalid literal for int() with base 10: {a}'
print("Thank You!") # this will get printed, and this shows program is not crashed