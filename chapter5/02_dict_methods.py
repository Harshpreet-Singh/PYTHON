d = {}   # d is empty dictionary

marks = {
    "Harsh": 100,
    "Rohan": 50,
    "Hari": 75,
    5:"anything",
    "else":[1,2,3]
}




print("\n")
print(marks)
 
# print(marks.items(), "\n") # RESULT= dict_items([('Harsh', 100), ('Rohan', 50), ('Hari', 75), (5, 'anything'), ('else', [1, 2, 3])])
# print(marks.keys()) # RESULT= dict_keys(['Harsh', 'Rohan', 'Hari', 5, 'else'])
# print(marks.values()) # RESULT= dict_values([100, 50, 75, 'anything', [1, 2, 3]])
# marks.update({"Hari": 80, "Harsh": 99, "added": "using .update"}) 
# .update is used to update any key or CAN ADD any key and value if does not exist

print("Value of Harsh is:",marks.get("Harsh")) #this will give you the value
print("Value of Rahul is:",marks.get("Rahul"), "\n")
# print(marks["x"]) this gives you error if 'x' does not exist
# print(marks.get("x")) This gives you "NONE" as response if 'x' does not exist

# print(marks.copy()) # provide you result 2 times

value = marks.get("Raul", 'NO raul DOES NOT EXIST')



print(value)


