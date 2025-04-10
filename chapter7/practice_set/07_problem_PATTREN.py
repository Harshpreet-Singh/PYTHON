n = int(input("Enter a Number: "))
for i in range(1, n+1):
    print(" "* (n-i), end="")     # end ="" this does not let print to add new line
    print("*"* (2*i-1), end="")
    print("")

print("Below is Without left space")


n = int(input("Enter a Number: "))
for i in range(1, n+1): 
    print("*"* (i), end="")
    '''or print("*"* (2*i-1), end="") '''
    print("")

