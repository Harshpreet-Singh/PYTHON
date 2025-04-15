try:
    a = int(input("Enter first Number: "))
    b = int(input("Enter second Number: "))
    print(a/b)
except ZeroDivisionError as v:
    print("Infinite")
    # print(v)