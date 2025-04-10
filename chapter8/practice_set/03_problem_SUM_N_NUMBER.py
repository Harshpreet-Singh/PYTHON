def sum(n):
        if(n == 1):
            return 1
        elif(n>1):
            return sum(n-1) + n

n = int(input("Enter a Number: "))
print(f"The Sum of {n} Natural Numbers is: {sum(n)}")
