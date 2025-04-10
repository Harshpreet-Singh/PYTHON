#  ////////////////////////////////------CREATE TUPLE HERE-------///////////////////////////////
name = []
students = []

n1 = input("ENTER STUDENT'S NAME: ")
name.append(n1)
m1 = int(input("ENTER MARKS here: "))
students.append(m1)

n2 = input("ENTER STUDENT'S NAME: ")
name.append(n2)
m2 = int(input("ENTER MARKS here: "))
students.append(m2)

n3 = input("ENTER STUDENT'S NAME: ")
name.append(n3)
m3 = int(input("ENTER MARKS here: "))
students.append(m3)

n4 = input("ENTER STUDENT'S NAME: ")
name.append(n4)
m4 = int(input("ENTER MARKS here: "))
students.append(m4)

n5 = input("ENTER STUDENT'S NAME: ")
name.append(n5)
m5 = int(input("ENTER MARKS here: "))
# students.append(m5)
students.sort()

#  ////////////////////////////////------AFTER VARIABLES HERE-------///////////////////////////////
marksheet = '''\t \tMARKS OF <|Name|> = <|Marks|> Marks'''


avg = ((m1+m2+m3+m4+m5)/2) 
no = (len(students))
#  ////////////////////////////////------PRINT HERE-------///////////////////////////////
print("\n" ,students, "\n")

print(f"NO.OF STUDENTS= {no} \n")

print(marksheet.replace("<|Name|>", n1).replace("<|Marks|>", str(m1)))
print(marksheet.replace("<|Name|>", n2).replace("<|Marks|>", str(m2)))
print(marksheet.replace("<|Name|>", n3).replace("<|Marks|>", str(m3)))
print(marksheet.replace("<|Name|>", n4).replace("<|Marks|>", str(m4)))
print(marksheet.replace("<|Name|>", n5).replace("<|Marks|>", str(m5)))

print(f"AVERAGE OF THEIR MARKS= {avg}")