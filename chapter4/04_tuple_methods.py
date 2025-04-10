a = (18,92,45,45,45,66,False,"Rohan","Shiv")
print(a)

no = a.count(45) # will count number of repititons
print(no, "\n")


i = (12,35,65,87,59,56,44,88)
print(12 in i, "\n") # if exists in tuple it returns True otherwise it will return false
print(len(i)) # it tells the length of tuple
print(i[1:5]) #will print from index 1 to index 5 

s = (1,2,3,4,5)
a,b,c,d,e = s           # THIS IS CALLED PACKING OF TUPLE 
print(a,b,c)            # if we will write till 'e' it will print till 5 (INSHORT = IT MATCHES THE INDEX NUMUBER)