name = input("Enter Your Name: ")
marks = int(input("Enter Your Marks: "))
phone = input("Enter Your Phone number: ")

if(len(phone) == 10) and phone.isdigit():
    print("The name of student is: {}, his marks are: {}, and his phone number is: {} ".format(name, marks, phone))
    student_data = {
        "Name of Sutudent: ": name,
        "Marks of Student: ": marks,
        "Phone Number: ": phone
        }
    with open("students.txt", "a") as f:
        f.write(str(student_data) + "\n")
    
    print("Data saved successfully!")
elif(len(phone) != 10):
    print("Enter a valid phone number! ")
else:
    print("Something went wrong!")




with open("students.txt", "r") as f:
    print(f.read())