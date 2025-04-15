try:
    a = int(input("Hey! Enter a Number: "))
    print(a)
except Exception as e:
    print(e)
else:
    print("I am inside else")

#  else will run if and only if try will run sucessfully, other wise it will not.