def pattren(n):
    if(n == 0):
        return 
    print("*" * n)
    pattren(n-1)

n = int(input("Enter a Number: "))
pattren(n)

'''
*******
******
*****
****
***
**
*


***
**
*


'''