n = int(input("Enter the number Here: "))
table = [n*i for i in range(1,11)]
print(table)
with open("chapter12\\practice_set\\tables.txt", "a") as t:
    t.write(f"Table of {n} is: {str(table)} \n")
inp = input("Do you want to clear the document ?(yes/no): ")
if inp.lower() == "yes":
    with open("chapter12\\practice_set\\tables.txt", "w") as t:
        t.truncate()
    print("Document cleared.")
elif inp.lower() == "no":
    print("Ok, Your document is not Cleared")
else:
    print("Something went wrong!")