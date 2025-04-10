marks = int(input("Enter your marks: "))

if(100>=marks>=90):
    grade =  "Your Grade is 'Ex'"

elif(90>marks>=80):
    grade = "Your Grade is 'A'"

elif(80>marks>=70):
    grade = "Your Grade is 'B'"

elif(70>marks>=60):
    grade = "Your Grade is 'C'"

elif(60>marks>=50):
    grade = "Your Grade is 'D'"

elif(marks>100):
    grade = "Enter Correct Marks"

else:
    grade = "You are Failed !"

print(grade)