n = int(input("Enter a Number: "))

for i in range(2, n):
    if(n%i == 0):
        print(f"{i+1} is not a Prime Number")       # if it is kept {i} it gives you correct answer it will show predecesor
        break
else:
    print(f"{i+1} is a Prime Number")