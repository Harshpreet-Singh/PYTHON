
def generateTable(n):
    table = ""
    for i in range(1,11):  # we needed tables from 1 to 10 
        table += f"{n} X {i} = {n*i}\n"
    with open(f"chapter9\\practice_set\\03_problem\\tables\\tables_{n}.txt", "w") as f:
        f.write(table)
        if(f"tables_{n}.txt" != ""):
            print(f"Tables of {n} Already exists")
        else:
            print("Created Files!")

for i in range(2, 21): # tables are from 2 to 20
    generateTable(i)