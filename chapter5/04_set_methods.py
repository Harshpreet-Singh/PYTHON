s = {1,2,32,46,5,5,5,"Harsh"}

s.add(96)

# print(s, type(s))

s1 = {1,45,6}
s2= {7,8,1,78}

st1 = {45, 6} # subset of s1
st2 = {1,45,6} # superset of s1

print(st1.issubset(s1)) # returns true 
print(st1.issuperset(s2)) # returns false 

print("\n\n\n")


print(s1.union(s2))  # this adds both the sets the prints them
print(s1.intersection(s2)) # this prints only the common values
print(s1-s2) 
print(s2-s2)  # this will give you set() as output
print(s2-s1) # subtract s1 from s1




