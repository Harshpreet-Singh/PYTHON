# length of username
username = input("Enter username: ")

if(len(username)<10):
    print("Your Username is too short \n It must of min 10 characters")
elif(' ' in username):
    print("No spaces are Allowed in Username")
else:
    print("All is Well")