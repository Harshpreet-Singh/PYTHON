#  FOLLOWING CONTAINS DEFAULT VALUES 

def greet_user(name, ending):
    print("Good Day, " + name)
    print(ending, "\n")

greet_user("Harshpreet", "Thank You")
greet_user("Rahul", "Thank You")


#  FOLLOWING WILL ASK THE USER TO ENTER THEIR NAMES


def goodDay(name, gender, end):
    if gender.lower() == "male":
        print(f"Hello, Mr."+name,"\n"+end)
    elif gender.lower() == "female":
        print(f"Hello, Ms."+name,"\n"+end)
    else:
        print(f"Hello, {name}")

# Get user details for the first user
name1 = input("Enter Name of User_1: ")
gender1 = input("Enter Your Gender: ")

# Get user details for the second user
name2 = input("Enter Name of User_2: ")
gender2 = input("Enter Your gender: ")

# Give user a Proper Salutation
end = "Have a Good Day"

goodDay(name1, gender1, end)
goodDay(name2, gender2, end)