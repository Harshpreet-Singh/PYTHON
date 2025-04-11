class Demo():
    a = 4

o = Demo()
print(o.a) # this will print 4 BECAUSE INSTANCE ATTRIBUTE IS NOT PRESENT
o.a = 0
print(o.a) # this is 0, as just above it is changed I.E. INSTANCE ATTRIBUTE HAS BEEN CHANGED
print(Demo.a) # this is also 4 i.e. class attr, this shows that class attribute is not changed, BUT INSTANCE ATTRIBUTE HAS BEEN CHANGED 