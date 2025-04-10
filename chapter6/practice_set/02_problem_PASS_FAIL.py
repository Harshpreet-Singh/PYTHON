# STUDENTS RESULT PASS OR FAIL

marks1 = int(input("Enter Marks 1: "))
marks2 = int(input("Enter Marks 2: "))
marks3 = int(input("Enter Marks 3: "))

# check for total percentage
total_percentage = (marks1 + marks2 + marks3)/3

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>= 33):
    print("YOU ARE PASS😎")

elif(marks1<33 or marks2<33 or marks3<33):
    print("YOU ARE FAILED!🤣")
    print("Marks in atleast one subject are less than 33")

else:
    print("YOU ARE FAILED!🤣, NEXT YEAR AANA \n", total_percentage, "% aye hai tere")

