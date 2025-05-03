def divisible5(n):
    if(n%5 == 0):
        return True
    return False

a = [1,2,15,10,52,48,45,89,90,78,70,78945,78541,45210,4580,5695]
f = list(filter(divisible5, a))
print(f)