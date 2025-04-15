dict1 = {"a":1, "b":2, "c":3}
dict2 = {"c": 4, "d": 6} 
# "c": 4   IS PRIORITIZED 
merged = dict1 | dict2 
print(merged)